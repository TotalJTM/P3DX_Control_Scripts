//Motor Pin Definitions
//motor control
#define PIN_L_motor_pwm 6
#define PIN_R_motor_pwm 5
#define PIN_motors_en 4
#define PIN_L_motor_dir 8
#define PIN_R_motor_dir 7
//motor encoder
#define PIN_L_encoder_A PC0
#define PIN_R_encoder_A PC1
#define PIN_R_encoder_B PC2
#define PIN_L_encoder_B PC3

//Ultra Sonic(US) Pin Definitions
//select bits
//#define PIN_US_A0 28
//#define PIN_US_A1 30
//#define PIN_US_A2 32
//control pins
//#define PIN_US_ping 10
//#define PIN_US_inhib 34
//#define PIN_US_echo 11

//User Control Interface Definitions
#define PIN_UI_reset_btn 3
#define PIN_UI_motors_btn 2
#define PIN_UI_aux1_btn 12
#define PIN_UI_aux2_btn 13
#define PIN_UI_buzzer 9
#define PIN_UI_power_LED 10
#define PIN_UI_status_LED 11

bool direct_drive = false;

//PID constants
double kp = 0.75;
double ki = 0.75;
double kd = 2;

//stores target speed and the speed calculated by left and right PID controllers
double left_speed = 0, right_speed = 0;
double target_left_speed = 0, target_right_speed = 0;

//motor encoder variables to track current and last encoder counts
//fun fact:  long integers can count up to 42 miles before overflowing, they dont need to be reset often
volatile long L_motor_encoder_count = 0, R_motor_encoder_count = 0;
volatile long L_last_encoder_count = 0, R_last_encoder_count = 0;
volatile uint8_t last_c_reg = PINC;

//== ISR vector handling encoder interrupt counting, also stores ==//
ISR(PCINT1_vect){
  uint8_t curr_c_reg = PINC;
  //check left encoder
  if((curr_c_reg&(1<<PIN_L_encoder_B)) != (last_c_reg&(1<<PIN_L_encoder_B))){
    if((curr_c_reg&(1<<PIN_L_encoder_B)) == (1<<PIN_L_encoder_B)){
      if(((curr_c_reg>>PIN_L_encoder_A)&0x01) == ((curr_c_reg>>PIN_L_encoder_B)&0x01))
        L_motor_encoder_count++;
      else
        L_motor_encoder_count--;
    }
    last_c_reg = curr_c_reg;
  }
  //check right encoder
  if((curr_c_reg&(1<<PIN_R_encoder_B)) != (last_c_reg&(1<<PIN_R_encoder_B))){
    if((curr_c_reg&(1<<PIN_R_encoder_B)) == (1<<PIN_R_encoder_B)){
      if(((curr_c_reg>>PIN_R_encoder_A)&0x01) == ((curr_c_reg>>PIN_R_encoder_B)&0x01))
        R_motor_encoder_count--;
      else
        R_motor_encoder_count++;
    }
    last_c_reg = curr_c_reg;
  }
  /*
  if(!(curr_c_reg&(1<<PIN_UI_reset_btn)))
    active_buttons |= (1<<PIN_UI_reset_btn);
  if(!(curr_c_reg&(1<<PIN_UI_motors_btn)))
    active_buttons |= (1<<PIN_UI_motors_btn);
  if(!(curr_c_reg&(1<<PIN_UI_aux1_btn)))
    active_buttons |= (1<<PIN_UI_aux1_btn);
  if(!(curr_c_reg&(1<<PIN_UI_aux2_btn)))
    active_buttons |= (1<<PIN_UI_aux2_btn);
    */
}
//==== PID Controller functions ====//
//taken from https://www.teachmemicro.com/arduino-pid-control-tutorial/
unsigned long currentTime;
double out;
//== Left controller function ==//
unsigned long  L_previousTime;
double L_elapsedTime, L_error, L_lastError, L_cumError, L_rateError;
double L_setPoint;
//computes the left PID speed based on current speed and target speed
void compute_left_PID(){     
  currentTime = millis();                                 //get current time
  L_elapsedTime = ((double)(currentTime - L_previousTime))/1000.0; //compute time elapsed from previous computation
        
  L_error = target_left_speed - left_speed;               // determine error
  L_cumError += L_error * L_elapsedTime;                  // compute integral
  L_rateError = (L_error - L_lastError)*L_elapsedTime;    // compute derivative
  //Serial.print(L_elapsedTime);Serial.print(" L ");
  //Serial.print(L_error);Serial.print("  ");Serial.print(kp*L_error);Serial.print(" | ");
  //Serial.print(L_cumError);Serial.print("  ");Serial.print(ki*L_error);Serial.print(" | ");
  //Serial.print(L_rateError);Serial.print("  ");Serial.println(kd*L_error);
  out = kp*L_error + ki*L_cumError + kd*L_rateError;      //PID output               
 
  L_lastError = L_error;                                  //remember current error
  L_previousTime = currentTime;                         //remember current time
 
  left_speed = out;                //have function set new left speed
}
//== Right controller function ==//
unsigned long  R_previousTime;
double R_elapsedTime, R_error, R_lastError, R_cumError, R_rateError;
double R_setPoint;
//computes the right PID speed based on current speed and target speed
void compute_right_PID(){     
  currentTime = millis();                                 //get current time
  R_elapsedTime = ((double)(currentTime - R_previousTime))/1000.0; //compute time elapsed from previous computation

  R_error = target_right_speed - right_speed;               // determine error
  R_cumError += R_error * R_elapsedTime;                  // compute integral
  R_rateError = (R_error - R_lastError)*R_elapsedTime;    // compute derivative
 //Serial.print(L_elapsedTime);Serial.print(" R ");Serial.print(L_error);Serial.print("  ");Serial.print(L_cumError);Serial.print("  ");Serial.println(L_rateError);
  out = kp*R_error + ki*R_cumError + kd*R_rateError;      //PID output               
 
  R_lastError = R_error;                                  //remember current error
  R_previousTime = currentTime;                         //remember current time
 
  right_speed = out;                                  //have function set new left speed
}

//== Robot specific variables to calculate robot distance traveled, in inches, since encoders reset ==//
const float ENCODER_TICKS_PER_ROTATION = 19105.0;
const float WHEEL_DIAM = 7.65;
const float IN_PER_TICK = (PI*WHEEL_DIAM);///float(ENCODER_TICKS_PER_ROTATION)
//function to convert current encoder ticks to inches
float convert_encoder_to_inches(long encoder_ticks){
  return IN_PER_TICK*(float(encoder_ticks)/ENCODER_TICKS_PER_ROTATION);
}

//== setup for main program ==//
void setup() {
  Serial.begin(115200);
  //motor pinmodes
  pinMode(PIN_L_motor_pwm, OUTPUT);       digitalWrite(PIN_L_motor_pwm, LOW);
  pinMode(PIN_R_motor_pwm, OUTPUT);       digitalWrite(PIN_R_motor_pwm, LOW);
  pinMode(PIN_motors_en, OUTPUT);         digitalWrite(PIN_motors_en, LOW);
  pinMode(PIN_L_motor_dir, OUTPUT);       digitalWrite(PIN_L_motor_dir, LOW);
  pinMode(PIN_R_motor_dir, OUTPUT);       digitalWrite(PIN_R_motor_dir, LOW);
  //motor encoder pinmodes
  pinMode(PIN_L_encoder_A, INPUT);
  pinMode(PIN_R_encoder_A, INPUT);
  pinMode(PIN_L_encoder_B, INPUT);
  pinMode(PIN_R_encoder_B, INPUT);//_PULLUP
  //interface control pinmodes
  pinMode(PIN_UI_reset_btn, INPUT);
  pinMode(PIN_UI_motors_btn, INPUT);
  pinMode(PIN_UI_aux1_btn, INPUT);
  pinMode(PIN_UI_aux2_btn, INPUT);
  pinMode(PIN_UI_buzzer, OUTPUT);
  pinMode(PIN_UI_status_LED, OUTPUT);

  //set up encoder ISR
  //will change depending on pin config (consult datasheet interrupts section)
  PCICR |= (1<<PCIE1);  //set PCINT Enable for C reg pins
  PCMSK1 |= (1<<PIN_L_encoder_B)|(1<<PIN_R_encoder_B);  //set the left and right encoder pin interrupts (interrupts on any pin change)

  //print statement that RPI uses to acknowledge robot is communicating properly
  Serial.println("<E,CONTROL_STARTED>");
}

// Serial communication buffers
const unsigned int BUFFER_SIZE = 256;
char message_buffer[BUFFER_SIZE];
char feedback_buffer[BUFFER_SIZE];
//function to handle a message from the RPI
void handle_message(){
  //search the buffer for the defined starting character < 
  char* last_token = strtok(message_buffer, "<");
  char* next_token;
  //get command from buffer
  long command = strtol(last_token, &next_token, 10);
  last_token = next_token + 1;
  //Serial.print("cmd: ");Serial.println(command, HEX);  
  if(command == 0){ //command does not do anything
    
  }else if(command == 10){ //changes motor speed, examples <10,40,40> <10,0,0>
    target_left_speed = double(strtol(last_token, &next_token, 10));
    last_token = next_token + 1;
    target_right_speed = double(strtol(last_token, &next_token, 10));
    last_token = next_token + 1;
    R_previousTime = millis();
    L_previousTime = millis();

    if(direct_drive == true){
      left_speed = target_left_speed;
      right_speed = target_right_speed;
      handle_motors();
    }
    //Serial.print(left_speed,DEC);Serial.print("  ");Serial.println(right_speed,DEC);
    //update_motors = true;
    //Serial.println("<10,OK>");
    
  }else if(command == 11){  //command formats message and sends encoder count to RPI
    Serial.print("<11,"); Serial.print(L_motor_encoder_count); Serial.print(","); Serial.print(R_motor_encoder_count);Serial.println(">");
  }else if(command == 12){  //command resets left and right encoder values if left and right reset vars are not zero <11,1,0>
    int left_encoder_reset = strtol(last_token, &next_token, 10);
    last_token = next_token + 1;
    int right_encoder_reset = strtol(last_token, &next_token, 10);
    last_token = next_token + 1;
    if(left_encoder_reset != 0) L_motor_encoder_count = 0;
    if(right_encoder_reset != 0) R_motor_encoder_count = 0;
    
  }else if(command == 90){  //encoder println divisions (message is sent to master every n encoder ticks) <12,0.1,0.1>
    //encoder_left_alert_in = strtod(last_token, &next_token);
    //last_token = next_token + 1;
    //encoder_right_alert_in = strtod(last_token, &next_token);
    //last_token = next_token + 1;
    //Serial.println("<12,OK>");
  }else if(command == 91){  //command overwrites current PID values 
    kp = strtod(last_token, &next_token);
    last_token = next_token + 1;
    ki = strtod(last_token, &next_token);
    last_token = next_token + 1;
    kd = strtod(last_token, &next_token);
    last_token = next_token + 1;
    //Serial.print("kp: ");Serial.print(kp);Serial.print("  ki: ");;Serial.print(ki);Serial.print("  kd: ");;Serial.print(kd);
  }else if(command == 92){  //command sets direct drive or PID drive
    int direct_drive_input = strtol(last_token, &next_token, 10);
    last_token = next_token + 1;
    if(direct_drive_input == 0){
      direct_drive = false;
    }else{
      direct_drive = true;
    }
  }
}

void handle_motors(){
  if(int(left_speed) != 0){
    analogWrite(PIN_L_motor_pwm,(1024/100)*abs(left_speed));
    if(left_speed > 0){
      digitalWrite(PIN_L_motor_dir, LOW);
    }else{
      digitalWrite(PIN_L_motor_dir, HIGH);
    }
  }else{
    analogWrite(PIN_L_motor_pwm,0);
    digitalWrite(PIN_L_motor_pwm, LOW);
  }

  if(int(right_speed) != 0){
    analogWrite(PIN_R_motor_pwm,(1024/100)*abs(right_speed));
    if(right_speed > 0){
      digitalWrite(PIN_R_motor_dir, HIGH);
    }else{
      digitalWrite(PIN_R_motor_dir, LOW);
    }
  }else{
    analogWrite(PIN_R_motor_pwm,0);
    digitalWrite(PIN_R_motor_pwm, LOW);
  }
  //update_motors = false;
}

//void rotate()

uint16_t encoder_message_interval = 200; //(ms) time between sending encoder message
uint32_t last_encoder_message = 0;

double acceptable_motor_speed_difference = 0.1;

bool last_reset_switch_state = digitalRead(PIN_UI_reset_btn);
bool last_motor_switch_state = digitalRead(PIN_UI_motors_btn);
bool last_aux1_switch_state = digitalRead(PIN_UI_aux1_btn);
bool last_aux2_switch_state = digitalRead(PIN_UI_aux2_btn);

void loop() {
  if (Serial.available() > 0) {
    unsigned int message_length = Serial.readBytesUntil('>', message_buffer, 256);
    if (message_length > 0) {
      //Serial.println(message_length);
      message_buffer[message_length] = '\0';
      //Serial.println(message_buffer);
      handle_message();
      //Serial.println(update_motors);Serial.println(right_speed);
      //if(update_motors == true) 
    }
  }
  if(abs(target_left_speed-left_speed) > acceptable_motor_speed_difference || abs(target_right_speed-right_speed) > acceptable_motor_speed_difference){
    compute_left_PID();
    compute_right_PID();
    if(left_speed > 101.0 || left_speed < -101.0 || left_speed > 101.0 || left_speed < -101.0){
      left_speed = 0.0;
      right_speed = 0.0;
      target_left_speed = 0.0;
      target_right_speed = 0.0;
    }
    //Serial.print("LA: ");Serial.print(left_speed);Serial.print("LT: ");Serial.print(target_left_speed);Serial.print("  |  ");Serial.print("RA: ");Serial.print(right_speed);Serial.print("RT: ");Serial.println(target_right_speed);
    handle_motors();
    
  }
  //check if any buttons are pressed and act accordingly
  bool pin_state; //assign variable once
  //handle reset state
  pin_state = digitalRead(PIN_UI_reset_btn);
  if(pin_state != last_reset_switch_state){
    last_reset_switch_state = pin_state;
  }
  //handle motors button state
  pin_state = digitalRead(PIN_UI_motors_btn);
  if(pin_state != last_motor_switch_state){
    if(pin_state == LOW){
      left_speed = 0.0;
      right_speed = 0.0;
      target_left_speed = 0.0;
      target_right_speed = 0.0;
      handle_motors();
      Serial.println("<99>");
    }
    last_motor_switch_state = pin_state;
  }
}
