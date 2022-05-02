//신발 코드
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
  digitalWrite(10, HIGH);
  digitalWrite(11, HIGH);
}

void turnOff(){ // 수동, 우산
  digitalWrite(10, LOW);
  digitalWrite(11, LOW);
}
