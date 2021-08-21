EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L P3-DX~Robot:PowerBoard P2
U 1 1 60EC83E8
P 5650 2050
F 0 "P2" H 5650 2875 50  0000 C CNN
F 1 "PowerBoard" H 5650 2784 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_2x13_P2.54mm_Vertical" H 5600 2750 50  0001 C CNN
F 3 "" H 5600 2750 50  0001 C CNN
	1    5650 2050
	1    0    0    -1  
$EndComp
$Comp
L P3-DX~Robot:InterfaceBoard P4
U 1 1 60EC920F
P 5650 4450
F 0 "P4" H 5650 5025 50  0000 C CNN
F 1 "InterfaceBoard" H 5650 4934 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_2x08_P2.54mm_Vertical" H 5750 4900 50  0001 C CNN
F 3 "" H 5750 4900 50  0001 C CNN
	1    5650 4450
	1    0    0    -1  
$EndComp
$Comp
L P3-DX~Robot:PowerPlug P1
U 1 1 60EC9D7D
P 5400 1000
F 0 "P1" H 5578 1051 50  0000 L CNN
F 1 "PowerPlug" H 5578 960 50  0000 L CNN
F 2 "Connector_Molex:Molex_Micro-Fit_3.0_43650-0415_1x04_P3.00mm_Vertical" H 5400 1200 50  0001 C CNN
F 3 "" H 5400 1200 50  0001 C CNN
	1    5400 1000
	1    0    0    -1  
$EndComp
$Comp
L P3-DX~Robot:SonarBoard P3
U 1 1 60ECA9CB
P 5650 3300
F 0 "P3" H 5650 3725 50  0000 C CNN
F 1 "SonarBoard" H 5650 3634 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_2x05_P2.54mm_Vertical" H 5650 3600 50  0001 C CNN
F 3 "" H 5650 3600 50  0001 C CNN
	1    5650 3300
	1    0    0    -1  
$EndComp
$Comp
L power:VPP #PWR0101
U 1 1 60ED70CB
P 5100 900
F 0 "#PWR0101" H 5100 750 50  0001 C CNN
F 1 "VPP" V 5100 1050 50  0000 L CNN
F 2 "" H 5100 900 50  0001 C CNN
F 3 "" H 5100 900 50  0001 C CNN
	1    5100 900 
	0    -1   -1   0   
$EndComp
$Comp
L power:VCC #PWR0102
U 1 1 60ED744A
P 5100 1100
F 0 "#PWR0102" H 5100 950 50  0001 C CNN
F 1 "VCC" V 5100 1250 50  0000 L CNN
F 2 "" H 5100 1100 50  0001 C CNN
F 3 "" H 5100 1100 50  0001 C CNN
	1    5100 1100
	0    -1   -1   0   
$EndComp
$Comp
L power:GND #PWR0103
U 1 1 60ED760E
P 4700 1100
F 0 "#PWR0103" H 4700 850 50  0001 C CNN
F 1 "GND" H 4705 927 50  0000 C CNN
F 2 "" H 4700 1100 50  0001 C CNN
F 3 "" H 4700 1100 50  0001 C CNN
	1    4700 1100
	1    0    0    -1  
$EndComp
Wire Wire Line
	4700 1100 4700 1000
Wire Wire Line
	4700 1000 5200 1000
Wire Wire Line
	5200 900  5100 900 
Wire Wire Line
	5200 1100 5100 1100
Wire Wire Line
	5200 2650 5100 2650
Wire Wire Line
	5100 2650 5100 2600
Wire Wire Line
	5100 2550 5200 2550
$Comp
L power:GND #PWR0104
U 1 1 60ED817E
P 5000 2600
F 0 "#PWR0104" H 5000 2350 50  0001 C CNN
F 1 "GND" H 5005 2427 50  0000 C CNN
F 2 "" H 5000 2600 50  0001 C CNN
F 3 "" H 5000 2600 50  0001 C CNN
	1    5000 2600
	1    0    0    -1  
$EndComp
Wire Wire Line
	5100 2600 5000 2600
Connection ~ 5100 2600
Wire Wire Line
	5100 2600 5100 2550
$Comp
L power:GND #PWR0105
U 1 1 60EDA7D0
P 5150 3600
F 0 "#PWR0105" H 5150 3350 50  0001 C CNN
F 1 "GND" H 5155 3427 50  0000 C CNN
F 2 "" H 5150 3600 50  0001 C CNN
F 3 "" H 5150 3600 50  0001 C CNN
	1    5150 3600
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0106
U 1 1 60EDC6FD
P 6500 3600
F 0 "#PWR0106" H 6500 3350 50  0001 C CNN
F 1 "GND" H 6505 3427 50  0000 C CNN
F 2 "" H 6500 3600 50  0001 C CNN
F 3 "" H 6500 3600 50  0001 C CNN
	1    6500 3600
	1    0    0    -1  
$EndComp
Text GLabel 6100 3500 2    50   Input ~ 0
S_ECHO
Wire Wire Line
	6500 3600 6500 3400
Wire Wire Line
	6500 3400 6050 3400
Wire Wire Line
	5250 3500 5150 3500
Wire Wire Line
	5150 3500 5150 3600
Wire Wire Line
	6100 3500 6050 3500
$Comp
L power:VCC #PWR0107
U 1 1 60EE09B2
P 5150 3400
F 0 "#PWR0107" H 5150 3250 50  0001 C CNN
F 1 "VCC" V 5150 3550 50  0000 L CNN
F 2 "" H 5150 3400 50  0001 C CNN
F 3 "" H 5150 3400 50  0001 C CNN
	1    5150 3400
	0    -1   -1   0   
$EndComp
$Comp
L power:VCC #PWR0108
U 1 1 60EE17E2
P 6150 3300
F 0 "#PWR0108" H 6150 3150 50  0001 C CNN
F 1 "VCC" V 6150 3450 50  0000 L CNN
F 2 "" H 6150 3300 50  0001 C CNN
F 3 "" H 6150 3300 50  0001 C CNN
	1    6150 3300
	0    1    1    0   
$EndComp
Wire Wire Line
	6150 3300 6050 3300
Wire Wire Line
	5250 3400 5150 3400
$Comp
L power:VCC #PWR0109
U 1 1 60EE2BAD
P 5150 4100
F 0 "#PWR0109" H 5150 3950 50  0001 C CNN
F 1 "VCC" V 5150 4250 50  0000 L CNN
F 2 "" H 5150 4100 50  0001 C CNN
F 3 "" H 5150 4100 50  0001 C CNN
	1    5150 4100
	0    -1   -1   0   
$EndComp
Wire Wire Line
	5250 4100 5150 4100
$Comp
L power:VCC #PWR0110
U 1 1 60EE3688
P 6150 4100
F 0 "#PWR0110" H 6150 3950 50  0001 C CNN
F 1 "VCC" V 6150 4250 50  0000 L CNN
F 2 "" H 6150 4100 50  0001 C CNN
F 3 "" H 6150 4100 50  0001 C CNN
	1    6150 4100
	0    1    1    0   
$EndComp
Wire Wire Line
	6150 4100 6050 4100
$Comp
L power:GND #PWR0111
U 1 1 60EE43D7
P 5100 4800
F 0 "#PWR0111" H 5100 4550 50  0001 C CNN
F 1 "GND" H 5105 4627 50  0000 C CNN
F 2 "" H 5100 4800 50  0001 C CNN
F 3 "" H 5100 4800 50  0001 C CNN
	1    5100 4800
	1    0    0    -1  
$EndComp
Wire Wire Line
	5250 4700 5100 4700
Wire Wire Line
	5100 4700 5100 4800
NoConn ~ 5250 4800
$Comp
L power:GND #PWR0112
U 1 1 60EE5B70
P 6150 4800
F 0 "#PWR0112" H 6150 4550 50  0001 C CNN
F 1 "GND" H 6155 4627 50  0000 C CNN
F 2 "" H 6150 4800 50  0001 C CNN
F 3 "" H 6150 4800 50  0001 C CNN
	1    6150 4800
	1    0    0    -1  
$EndComp
Wire Wire Line
	6050 4600 6150 4600
Wire Wire Line
	6150 4600 6150 4800
Text GLabel 5100 1750 0    50   Input ~ 0
E-STOP
Text GLabel 6200 1450 2    50   Input ~ 0
LEFT_MOTOR_DIR
Text GLabel 6200 1550 2    50   Input ~ 0
RIGHT_MOTOR_DIR
Text GLabel 6200 1650 2    50   Input ~ 0
LEFT_ENCODER_A
Text GLabel 6200 1750 2    50   Input ~ 0
RIGHT_ENCODER_A
Text GLabel 6200 1850 2    50   Input ~ 0
RIGHT_ENCODER_B
Text GLabel 6200 1950 2    50   Input ~ 0
LEFT_ENCODER_B
Wire Wire Line
	6200 1450 6100 1450
Wire Wire Line
	6100 1550 6200 1550
Wire Wire Line
	6200 1650 6100 1650
Wire Wire Line
	6100 1750 6200 1750
Wire Wire Line
	6200 1850 6100 1850
Wire Wire Line
	6100 1950 6200 1950
Wire Wire Line
	5200 1750 5100 1750
Wire Wire Line
	5100 1650 5200 1650
Wire Wire Line
	5200 1550 5100 1550
Wire Wire Line
	5100 1450 5200 1450
NoConn ~ 6050 4800
NoConn ~ 6050 4700
Text GLabel 6150 4500 2    50   Input ~ 0
STATUS_LED
Text GLabel 6150 4400 2    50   Input ~ 0
BUZZER
Text GLabel 6150 4300 2    50   Input ~ 0
AUX_SWITCH
Text GLabel 6150 4200 2    50   Input ~ 0
MOTOR_SWITCH
Text GLabel 5150 4200 0    50   Input ~ 0
RESET_SWITCH
Text GLabel 5150 4300 0    50   Input ~ 0
RADIO_SWITCH
Text GLabel 5150 4500 0    50   Input ~ 0
POWER_LED
Wire Wire Line
	6150 4200 6050 4200
Wire Wire Line
	6050 4300 6150 4300
Wire Wire Line
	6150 4400 6050 4400
Wire Wire Line
	6050 4500 6150 4500
Wire Wire Line
	5250 4500 5150 4500
Wire Wire Line
	5150 4300 5250 4300
Wire Wire Line
	5250 4200 5150 4200
$Comp
L power:VPP #PWR0113
U 1 1 60FCE9FB
P 6200 2450
F 0 "#PWR0113" H 6200 2300 50  0001 C CNN
F 1 "VPP" V 6200 2600 50  0000 L CNN
F 2 "" H 6200 2450 50  0001 C CNN
F 3 "" H 6200 2450 50  0001 C CNN
	1    6200 2450
	0    1    1    0   
$EndComp
Wire Wire Line
	6200 2450 6100 2450
$Comp
L power:VPP #PWR0114
U 1 1 60FD2E35
P 5150 4600
F 0 "#PWR0114" H 5150 4450 50  0001 C CNN
F 1 "VPP" V 5150 4750 50  0000 L CNN
F 2 "" H 5150 4600 50  0001 C CNN
F 3 "" H 5150 4600 50  0001 C CNN
	1    5150 4600
	0    -1   -1   0   
$EndComp
Wire Wire Line
	5250 4600 5150 4600
NoConn ~ 5250 4400
NoConn ~ 6100 2550
NoConn ~ 6100 2650
NoConn ~ 6100 2350
NoConn ~ 6100 2250
NoConn ~ 6100 2150
NoConn ~ 6100 2050
NoConn ~ 5200 2150
NoConn ~ 5200 2250
NoConn ~ 5200 2350
NoConn ~ 5200 2450
NoConn ~ 5200 1850
Text GLabel 5150 3100 0    50   Input ~ 0
S_SEL1
Text GLabel 5150 3200 0    50   Input ~ 0
S_SEL3
Text GLabel 6150 3100 2    50   Input ~ 0
S_SEL2
Wire Wire Line
	5250 3100 5150 3100
Wire Wire Line
	5250 3200 5150 3200
Wire Wire Line
	6050 3100 6150 3100
Text GLabel 5150 3300 0    50   Input ~ 0
S_TRIG
Text GLabel 6150 3200 2    50   Input ~ 0
S_INHIB
Wire Wire Line
	6150 3200 6050 3200
Wire Wire Line
	5250 3300 5150 3300
$Comp
L MCU_Microchip_ATtiny:ATtiny84-20PU U1
U 1 1 61008865
P 2700 4650
F 0 "U1" H 2170 4696 50  0000 R CNN
F 1 "ATtiny84-20PU" H 2170 4605 50  0000 R CNN
F 2 "Package_DIP:DIP-14_W7.62mm" H 2700 4650 50  0001 C CIN
F 3 "http://ww1.microchip.com/downloads/en/DeviceDoc/doc8006.pdf" H 2700 4650 50  0001 C CNN
	1    2700 4650
	-1   0    0    -1  
$EndComp
Text GLabel 2000 2450 0    50   Input ~ 0
STATUS_LED
Text GLabel 2000 2350 0    50   Input ~ 0
POWER_LED
Text GLabel 2000 2250 0    50   Input ~ 0
BUZZER
Text GLabel 3200 2350 2    50   Input ~ 0
SDA
Text GLabel 3200 2450 2    50   Input ~ 0
SCL
Wire Wire Line
	2100 2150 2000 2150
Wire Wire Line
	2000 2050 2100 2050
Wire Wire Line
	2100 1950 2000 1950
Wire Wire Line
	2000 1850 2100 1850
Wire Wire Line
	2100 1750 2000 1750
Wire Wire Line
	2100 1650 2000 1650
Wire Wire Line
	2000 1550 2100 1550
Wire Wire Line
	3200 2450 3100 2450
Wire Wire Line
	3100 2350 3200 2350
Text GLabel 2000 2550 0    50   Input ~ 0
AUX_SWITCH
Text GLabel 2000 2650 0    50   Input ~ 0
RADIO_SWITCH
Text GLabel 2000 1550 0    50   Input ~ 0
MOTOR_SWITCH
Text GLabel 2000 1650 0    50   Input ~ 0
RESET_SWITCH
Text GLabel 2000 1750 0    50   Input ~ 0
MOTORS_ENABLED
Text GLabel 2000 1850 0    50   Input ~ 0
RIGHT_MOTOR_PWM
Text GLabel 2000 1950 0    50   Input ~ 0
LEFT_MOTOR_PWM
Text GLabel 2000 2050 0    50   Input ~ 0
RIGHT_MOTOR_DIR
Text GLabel 2000 2150 0    50   Input ~ 0
LEFT_MOTOR_DIR
Wire Wire Line
	2000 1450 2100 1450
Wire Wire Line
	2100 1350 2000 1350
Text GLabel 2000 1350 0    50   Input ~ 0
SERIAL_IN
Text GLabel 2000 1450 0    50   Input ~ 0
SERIAL_OUT
Wire Wire Line
	3200 2250 3100 2250
Wire Wire Line
	3100 2150 3200 2150
Wire Wire Line
	3200 2050 3100 2050
Wire Wire Line
	3100 1950 3200 1950
Text GLabel 3200 2150 2    50   Input ~ 0
RIGHT_ENCODER_B
Text GLabel 3200 2050 2    50   Input ~ 0
RIGHT_ENCODER_A
Text GLabel 3200 1950 2    50   Input ~ 0
LEFT_ENCODER_A
Text GLabel 3200 2250 2    50   Input ~ 0
LEFT_ENCODER_B
NoConn ~ 2800 950 
NoConn ~ 2700 950 
Wire Wire Line
	2500 950  2500 850 
$Comp
L power:VCC #PWR0115
U 1 1 60FDE6EF
P 2500 850
F 0 "#PWR0115" H 2500 700 50  0001 C CNN
F 1 "VCC" V 2500 1000 50  0000 L CNN
F 2 "" H 2500 850 50  0001 C CNN
F 3 "" H 2500 850 50  0001 C CNN
	1    2500 850 
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0116
U 1 1 60FDDF0E
P 2600 3150
F 0 "#PWR0116" H 2600 2900 50  0001 C CNN
F 1 "GND" H 2600 2950 50  0000 C CNN
F 2 "" H 2600 3150 50  0001 C CNN
F 3 "" H 2600 3150 50  0001 C CNN
	1    2600 3150
	1    0    0    -1  
$EndComp
Wire Wire Line
	2600 3150 2500 3150
Connection ~ 2600 3150
Wire Wire Line
	2600 3050 2600 3150
Wire Wire Line
	2500 3150 2500 3050
Wire Wire Line
	2700 3150 2600 3150
Wire Wire Line
	2700 3050 2700 3150
Text GLabel 5100 1650 0    50   Input ~ 0
MOTORS_ENABLED
Text GLabel 5100 1550 0    50   Input ~ 0
RIGHT_MOTOR_PWM
Text GLabel 5100 1450 0    50   Input ~ 0
LEFT_MOTOR_PWM
$Comp
L MCU_Module:Arduino_UNO_R3 A1
U 1 1 60EF8F76
P 2600 1950
F 0 "A1" H 2600 3131 50  0000 C CNN
F 1 "Arduino_UNO_R3" H 2600 3040 50  0000 C CNN
F 2 "Module:Arduino_UNO_R3" H 2600 1950 50  0001 C CIN
F 3 "https://www.arduino.cc/en/Main/arduinoBoardUno" H 2600 1950 50  0001 C CNN
	1    2600 1950
	1    0    0    -1  
$EndComp
$Comp
L power:VCC #PWR0117
U 1 1 6101EB37
P 2700 3650
F 0 "#PWR0117" H 2700 3500 50  0001 C CNN
F 1 "VCC" H 2650 3800 50  0000 L CNN
F 2 "" H 2700 3650 50  0001 C CNN
F 3 "" H 2700 3650 50  0001 C CNN
	1    2700 3650
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0118
U 1 1 6102A024
P 2700 5650
F 0 "#PWR0118" H 2700 5400 50  0001 C CNN
F 1 "GND" H 2700 5450 50  0000 C CNN
F 2 "" H 2700 5650 50  0001 C CNN
F 3 "" H 2700 5650 50  0001 C CNN
	1    2700 5650
	1    0    0    -1  
$EndComp
Wire Wire Line
	2700 5650 2700 5550
NoConn ~ 3100 1550
NoConn ~ 3100 1750
Wire Wire Line
	2000 2250 2100 2250
Wire Wire Line
	2100 2350 2000 2350
Wire Wire Line
	2000 2450 2100 2450
Wire Wire Line
	2100 2550 2000 2550
Wire Wire Line
	2000 2650 2100 2650
Text GLabel 2000 4650 0    50   Input ~ 0
SDA
Wire Wire Line
	2100 4450 2000 4450
Wire Wire Line
	2000 4650 2100 4650
Text GLabel 2000 4550 0    50   Input ~ 0
S_TRIG
Text GLabel 2000 4050 0    50   Input ~ 0
S_SEL1
Text GLabel 2000 4150 0    50   Input ~ 0
S_SEL2
Text GLabel 2000 4250 0    50   Input ~ 0
S_SEL3
Text GLabel 2000 4350 0    50   Input ~ 0
S_INHIB
Text GLabel 2000 4450 0    50   Input ~ 0
S_ECHO
Wire Wire Line
	2100 4350 2000 4350
Wire Wire Line
	2000 4550 2100 4550
Wire Wire Line
	2100 4250 2000 4250
Wire Wire Line
	2000 4150 2100 4150
Wire Wire Line
	2100 4050 2000 4050
Wire Wire Line
	2100 5150 2000 5150
Text GLabel 3200 1350 2    50   Input ~ 0
RESET
Text GLabel 2000 5250 0    50   Input ~ 0
RESET
Wire Wire Line
	2100 5250 2000 5250
Wire Wire Line
	3200 1350 3100 1350
Text GLabel 2000 5150 0    50   Input ~ 0
SCL
$Comp
L power:GND #PWR0119
U 1 1 6105F905
P 1850 4800
F 0 "#PWR0119" H 1850 4550 50  0001 C CNN
F 1 "GND" H 1850 4600 50  0000 C CNN
F 2 "" H 1850 4800 50  0001 C CNN
F 3 "" H 1850 4800 50  0001 C CNN
	1    1850 4800
	1    0    0    -1  
$EndComp
Wire Wire Line
	2100 4750 2000 4750
Wire Wire Line
	2100 5050 2000 5050
Wire Wire Line
	2000 5050 2000 4950
Wire Wire Line
	2000 4950 2100 4950
Wire Wire Line
	2000 4950 2000 4750
Connection ~ 2000 4950
Wire Wire Line
	1850 4800 1850 4750
Wire Wire Line
	1850 4750 2000 4750
Connection ~ 2000 4750
$Comp
L Device:C_Small C1
U 1 1 6107057F
P 3050 3700
F 0 "C1" V 2821 3700 50  0000 C CNN
F 1 "10uF" V 2912 3700 50  0000 C CNN
F 2 "Capacitor_SMD:C_1206_3216Metric_Pad1.33x1.80mm_HandSolder" H 3050 3700 50  0001 C CNN
F 3 "~" H 3050 3700 50  0001 C CNN
	1    3050 3700
	0    1    1    0   
$EndComp
$Comp
L power:GND #PWR0120
U 1 1 61073AFF
P 3350 3850
F 0 "#PWR0120" H 3350 3600 50  0001 C CNN
F 1 "GND" H 3350 3650 50  0000 C CNN
F 2 "" H 3350 3850 50  0001 C CNN
F 3 "" H 3350 3850 50  0001 C CNN
	1    3350 3850
	1    0    0    -1  
$EndComp
Wire Wire Line
	3350 3700 3350 3850
Wire Wire Line
	2700 3650 2700 3700
Wire Wire Line
	3150 3700 3350 3700
Wire Wire Line
	2950 3700 2700 3700
Connection ~ 2700 3700
Wire Wire Line
	2700 3700 2700 3750
$EndSCHEMATC