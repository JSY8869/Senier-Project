char shoe_start = '1';
void setup() {
  pinMode(10, OUTPUT);      // 출력핀 설정
  pinMode(11, OUTPUT);
  Serial.begin(9600);           
}

void loop() {
  char a = Serial.read();
  int sign = strcmp(&a,&shoe_start);
  if(sign == 0){
    turnOn();
  }else{
    turnOff();
  }
  delay(10);
}

void turnOn(){ // 수동, 우산
  analogWrite(10, 255);
  analogWrite(11, 255);
}

void turnOff(){ // 수동, 우산
  analogWrite(10, 0);
  analogWrite(11, 0);
}
