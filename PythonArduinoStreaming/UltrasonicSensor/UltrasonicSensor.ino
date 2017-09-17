const int trigPin = 9;
const int echoPin = 10;
#include <Servo.h>


int servoPin = 9;
long duration;
int distance;
Servo myservo;  
 
int angle = 0;   // servo position in degrees 
 
void setup() 
{ 
  myservo.attach(servoPin); 

// defines variables

pinMode(trigPin, OUTPUT); 
pinMode(echoPin, INPUT); 
Serial.begin(9600); 
}
void loop() {
if(Serial.read()== -1){
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  
  duration = pulseIn(echoPin, HIGH);
  
  distance= duration*0.034/2;
  if (distance < 10){
    Serial.println(true);
    delay(1000);
  }
}
else{myservo.write(45);
    delay(1500);
    myservo.write(90);    
    delay(100);
    myservo.write(125); 
    delay(400);
    delay(1500);
  }
}


