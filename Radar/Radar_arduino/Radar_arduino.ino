#include <Servo.h>
Servo servo_1;
#define echoPin 12
#define trigPin 13
long sure, mesafe; //süre ve uzaklık diye iki değişken tanımlıyoruz.
float aci=0;
void setup() {
  // put your setup code here, to run once:
Serial.begin(19200);
pinMode(echoPin, INPUT);
pinMode(trigPin, OUTPUT);
servo_1.attach(9);
}
void loop() {

digitalWrite(trigPin, LOW); //sensör pasif hale getirildi
delayMicroseconds(5);
digitalWrite(trigPin, HIGH); //Sensore ses dalgasının üretmesi için emir verildi
delayMicroseconds(10);
digitalWrite(trigPin, LOW); //Yeni dalgaların üretilmemesi için trig pini LOW konumuna getirildi
sure = pulseIn(echoPin, HIGH); //ses dalgasının geri dönmesi için geçen sure ölçülüyor
delay(10);
mesafe = sure / 29.1 / 2; //ölçülen süre uzaklığa çevriliyor
if(mesafe>80){
  mesafe=0;
  }
Serial.println(String(mesafe)+','+String(aci));
servo_1.write(aci);
delay(15);
aci=aci+1;
if(aci>180){
  aci=0;
  delay(80);
  }
mesafe=0;
delay(120);
}
