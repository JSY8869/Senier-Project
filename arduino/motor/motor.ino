#include <Servo.h>
Servo myservo;
char shoe_start = '1';
void setup() {
  myservo.attach(2);
  Serial.begin(9600);           
}

void loop() {
  char a = Serial.read();
  int sign = strcmp(&a,&shoe_start);
  if(sign == 0){
    turn1();
    turn2();
  }
}

void turn1(){ // 수동, 우산
  for(int i = 0; i < 100; i++){
      char a = Serial.read();
      int sign = strcmp(&a,&shoe_start);
      if(sign == 1){break;}
      myservo.write(180);
    delay(10);
  }
}

void turn2(){ // 수동, 우산
  for(int i = 0; i < 100; i++){
      char a = Serial.read();
      int sign = strcmp(&a,&shoe_start);
      if(sign == 1){break;}
      myservo.write(0);
    delay(10);
  }
}
