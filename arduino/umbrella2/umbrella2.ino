#include <Wire.h>

void setup() {
  pinMode(10, OUTPUT);      // 출력핀 설정
  pinMode(11, OUTPUT);
  Wire.begin(2); //슬레이브 주소                
  Wire.onReceive(receiveEvent); //데이터 전송 받을 때 receiveEvent함수 호출
  Serial.begin(9600);           
}

void loop() {
  
}

void receiveEvent(int recieve) { //전송 데이터 읽기
  int x = Wire.read();
  if(x==1){
    cool();
  }else{
    hot();
    }
}


void cool(){
  analogWrite(10, 255);
  analogWrite(11, 255);
  }

void hot(){
  analogWrite(10, 0);
  analogWrite(11, 0);
}
