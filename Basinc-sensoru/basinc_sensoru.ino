
#include <Wire.h>
#include <LiquidCrystal.h>
#include <SFE_BMP180.h>
LiquidCrystal lcd(12,11,5,4,3,2);
int sure=0;
bool i=1;
bool i2=1;
bool i3=1;
int input,working_mode;
double T, P, p0,a;
SFE_BMP180 bmp180;  // bmp180 adında bir sensör nesnesi oluştur
void setup() {
  lcd.begin(16,2);
  Serial.begin(19200);
  bmp180.begin();
}
void loop() {
  while (i){
  if(Serial.available() and i){
        input =  Serial.parseInt();
        i=0;
  }
    }
  if(i2){delay(1000);}
  while (i2){
  if(Serial.available() and i2){
        working_mode =  Serial.parseInt();
        i2=0;
  }
    }
    
 if (working_mode==2 and i3){
    delay(250);
    bmp180.startTemperature();
    delay(250);
    bmp180.getTemperature(T);
    delay(250);
    bmp180.startPressure(3);
    delay(250);
    bmp180.getPressure(P, T);
    input=P;
    i3=0;
  } 
    bmp180.startTemperature();
    delay(250);
    bmp180.getTemperature(T);
    delay(250);
    bmp180.startPressure(3);
    delay(250);
    bmp180.getPressure(P, T);
    a = bmp180.altitude(P,input);
    p0 = bmp180.sealevel(P,input);
    sure=sure+1;
    delay(250);
    if (working_mode==1){   
    Serial.print(p0);
    }
    else{
      Serial.print(a);
      }
    Serial.print(",");
    Serial.print(T);
    Serial.print(",");
    Serial.println(sure);
    lcd.setCursor(0, 0);
    if (working_mode==1){   
    lcd.print("Basinc:"+String(p0));
    }
    else{
      lcd.print("Irtifa:"+String(a));
      }
    lcd.setCursor(0, 1);
    lcd.print("Sicaklik:"+String(T));
        
    
    
  
}
