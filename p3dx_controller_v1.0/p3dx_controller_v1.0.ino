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

long left_speed = 0, right_speed = 0;
long encoder_left_divisions = 0, encoder_right_divisions = 0;
float encoder_left_alert_in = 0.0, encoder_right_alert_in = 0.0;
float last_encoder_left_alert_in = 0.0, last_encoder_right_alert_in = 0.0;

volatile long L_motor_encoder_count = 0;
volatile long R_motor_encoder_count = 0;
volatile uint8_t last_c_reg = PINC;
volatile bool left_enc_flag = false, right_enc_flag = false;
volatile long L_last_encoder_count = 0;
volatile long R_last_encoder_count = 0;

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
  if(encoder_left_divisions != 0 && L_motor_encoder_count > L_last_encoder_count+encoder_left_divisions){
    L_last_encoder_count = L_motor_encoder_count;
    left_enc_flag = true;
  }
  if(encoder_right_divisions != 0 && R_motor_encoder_count > R_last_encoder_count+encoder_right_divisions){
    R_last_encoder_count = R_motor_encoder_count;
    right_enc_flag = true;
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

const float ENCODER_TICKS_PER_ROTATION = 19105.0;
const float WHEEL_DIAM = 7.65;
const float IN_PER_TICK = (PI*WHEEL_DIAM);///float(ENCODER_TICKS_PER_ROTATION)

float convert_encoder_to_inches(long encoder_ticks){
  return IN_PER_TICK*(float(encoder_ticks)/ENCODER_TICKS_PER_ROTATION);
}

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
  PCICR |= (1<<PCIE1);
  PCMSK1 |= (1<<PIN_L_encoder_B)|(1<<PIN_R_encoder_B);//(1<<PIN_L_encoder_A)|(1<<PIN_R_encoder_A)

  Serial.println("<E,CONTROL_STARTED>");
  //Serial.println(IN_PER_TICK);

}

// Serial communication buffers
const unsigned int BUFFER_SIZE = 256;
char message_buffer[BUFFER_SIZE];
char feedback_buffer[BUFFER_SIZE];

bool update_motors = true;

void handle_message(){
  char* last_token = strtok(message_buffer, "<");
  char* next_token;

  long command = strtol(last_token, &next_token, 10);
  last_token = next_token + 1;
  //Serial.print("cmd: ");Serial.println(command, HEX);  //<10,40,40> <10,0,0>
  if(command == 0){
    //Serial.println("<0,INVALID COMMAND>");
  }else if(command == 10){
    left_speed = strtol(last_token, &next_token, 10);
    last_token = next_token + 1;
    right_speed = strtol(last_token, &next_token, 10);
    last_token = next_token + 1;
    
    //Serial.print(left_speed,DEC);Serial.print("  ");Serial.println(right_speed,DEC);
    update_motors = true;
    //Serial.println("<10,OK>");
  }else if(command == 11){  //encoder println divisions (message is sent to master every n encoder ticks) <11,1000,1000>
    encoder_left_divisions = strtol(last_token, &next_token, 10);
    last_token = next_token + 1;
    encoder_right_divisions = strtol(last_token, &next_token, 10);
    last_token = next_token + 1;
    //Serial.println("<11,OK>");
  }else if(command == 12){  //encoder println divisions (message is sent to master every n encoder ticks) <12,0.1,0.1>
    encoder_left_alert_in = strtod(last_token, &next_token);
    last_token = next_token + 1;
    encoder_right_alert_in = strtod(last_token, &next_token);
    last_token = next_token + 1;
    //Serial.println("<12,OK>");
  }
}

void handle_motors(){
  if(left_speed != 0){
    if(left_speed < -100 || left_speed > 100)
      left_speed = constrain(left_speed, -100, 100);
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

  if(right_speed != 0){
    if(right_speed < -100 || right_speed > 100)
      right_speed = constrain(right_speed, -100, 100);
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
  update_motors = false;
}

//void rotate()


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
      handle_motors();
    }
  }
  
  if(left_enc_flag == true){
    Serial.print("<11,L:"); Serial.print(L_motor_encoder_count); Serial.println(">");
    left_enc_flag = false;
  }
  if(right_enc_flag == true){
    Serial.print("<11,R:"); Serial.print(R_motor_encoder_count); Serial.println(">");
    right_enc_flag = false;
  }

  float current_encoder_in_left = convert_encoder_to_inches(L_motor_encoder_count);
  float current_encoder_in_right = convert_encoder_to_inches(R_motor_encoder_count);
  //Serial.println(current_encoder_in_left);
  if(encoder_left_alert_in != 0.0 && current_encoder_in_left >= encoder_left_alert_in+last_encoder_left_alert_in){
    last_encoder_left_alert_in = current_encoder_in_left;
    Serial.print("<12,R:"); Serial.print(current_encoder_in_left); Serial.println(">");
  }
  
  //analogWrite(PIN_L_motor_pwm,1023/10);
  //analogWrite(PIN_R_motor_pwm,1023/10);
  //digitalWrite(PIN_L_motor_dir, HIGH);
  //digitalWrite(PIN_R_motor_dir, LOW);
  //Serial.println(convert_encoder_to_inches(R_motor_encoder_count));
  //Serial.println(R_motor_encoder_count);


}
