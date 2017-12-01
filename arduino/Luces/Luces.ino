#include <Servo.h>
#include <dht.h>
Servo servoMotor;
dht DHT;
#define DHT11_PIN A0
dht other_dht;
#define DHT11_PIN A1
int servo_one = 10;
int Echo =12;
int Trigger = 13;
int tiempo,distancia;
char list_string[20]; 
char inChar=-1; 
byte index = 0;

void setup(){
  pinMode(Echo,INPUT);
  pinMode(Trigger,OUTPUT);
  servoMotor.attach(10);
  servoMotor.write(95);
  Serial.begin(115200);
  pinMode(11,OUTPUT);
  pinMode(9,OUTPUT);
  pinMode(8,OUTPUT);
  pinMode(7,OUTPUT);
  pinMode(6,OUTPUT);
  pinMode(5,OUTPUT);
  pinMode(4,OUTPUT);
  pinMode(3,OUTPUT);
  pinMode(2,OUTPUT);
}

char Comp(char* Flag){

 while(Serial.available() > 0)
 {
   if(index < 19) 
   {
     inChar = Serial.read();
     list_string[index] = inChar; 
     index++; 
     list_string[index] = '\0'; 
   }
 }

 if(strcmp(list_string,Flag) == 0){
   for(int i=0;i<19;i++){
     list_string[i]=0;
   }
   index=0;
   return(0);
 }
 else{
   return(1);
 }
}

void calculateDistance(int tiempo){
  distancia = (tiempo/2)/29.1;
  if (distancia<0 || distancia > 50){
    distancia = 0;
    sendtemperatureData(distancia);
  }
  else{
    sendtemperatureData(distancia);
  }
}

void sendData(int distancia, int temp_one, int temp_two){
  Serial.print(distancia);
  Serial.print(",");
  Serial.print(temp_one);
  Serial.print(",");
  Serial.println(temp_two);
  delay(50);
}

void sendtemperatureData(int distance){
  int chk = DHT.read11(DHT11_PIN);
  delay(200);
  int temp = other_dht.read11(DHT11_PIN);
  delay(200);
  int temp_one =DHT.temperature;
  int temp_two = other_dht.temperature;
  sendData(distance,temp_one, temp_two);
  
  }


void loop()
{
  digitalWrite(Trigger,LOW);
  delayMicroseconds(5);
  digitalWrite(Trigger,HIGH);
  delayMicroseconds(10);
  digitalWrite(Trigger,LOW);
  tiempo = pulseIn(Echo,HIGH);
  calculateDistance(tiempo);
  
  if (Comp("True")== 0){
   servoMotor.write(0);
  }
  else if (Comp("False") == 0){
   servoMotor.write(95);
  }
  else if (Comp("1F") == 0){
   digitalWrite(8,HIGH);
  
  }
  else if (Comp("0F") == 0){
   digitalWrite(8,LOW);
  }
 
  else if (Comp("1C") == 0){
   digitalWrite(7,HIGH);
  }
 
  else if (Comp("0C") == 0){
   digitalWrite(7,LOW);
 }
 
  else if (Comp("1A") == 0){
   digitalWrite(6,HIGH);
 }
 
  else if (Comp("0A") == 0){
   digitalWrite(6,LOW);
 }
 
  else if (Comp("1B") == 0){
   digitalWrite(5,HIGH);
 }
 
  else if (Comp("0B") == 0){
   digitalWrite(5,LOW);
 }
 
  else if (Comp("1E") == 0){
   digitalWrite(4,HIGH);
 }
 
  else if (Comp("0E") == 0){
   digitalWrite(4,LOW);
 }
 
  else if (Comp("1G") == 0){
   digitalWrite(3,HIGH);
 }
 
  else if (Comp("0G") == 0){
   digitalWrite(3,LOW);
 }
 
  else if (Comp("1D") == 0){
   digitalWrite(2,HIGH);
 }
 
  else if (Comp("0D") == 0){
   digitalWrite(2,LOW);
 }
 
  else if (Comp("1H")== 0){
   digitalWrite(8,LOW);
   digitalWrite(7,LOW);
   digitalWrite(6,LOW);
   digitalWrite(5,LOW);
   digitalWrite(4,LOW);
   digitalWrite(3,LOW);
   digitalWrite(2,LOW);
  }
  else if (Comp("fan_one_on") == 0){
   digitalWrite(11,HIGH);
  }
  else if (Comp("fan_one_off") == 0){
   digitalWrite(11,LOW);
  }
  else if (Comp("fan_two_on") == 0){
   digitalWrite(9,HIGH);
  }
  else if (Comp("fan_two_off") == 0){
   digitalWrite(9,LOW);
  }
  else if (Comp("all_fans_off") == 0){
   digitalWrite(9,LOW);
   digitalWrite(11,LOW);
  }
  else if (Comp("all_fans_on") == 0){
   digitalWrite(9,HIGH);
   digitalWrite(11,HIGH);
  }
  
}  



