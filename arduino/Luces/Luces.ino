int led1 = 8;
int led2 = 7;
int led3 = 6;
int led4 = 5;
int led5 = 4;
int led6 = 3;
int led7 = 2;
int state1 = 0;
int state2 = 0;
int state3 = 0;
int state4 = 0;
int state5 = 0;
int state6 = 0;
int state7 = 0;

void setup() {
   Serial.begin(115200);
   pinMode(led1, OUTPUT);
   digitalWrite(led1, LOW);
   pinMode(led2, OUTPUT);
   digitalWrite(led2, LOW);
   pinMode(led3, OUTPUT);
   digitalWrite(led3, LOW);
   pinMode(led4, OUTPUT);
   digitalWrite(led4, LOW);
   pinMode(led5, OUTPUT);
   digitalWrite(led5, LOW);
   pinMode(led6, OUTPUT);
   digitalWrite(led6, LOW);
   pinMode(led7, OUTPUT);
   digitalWrite(led7, LOW);
}

void loop() { }

void serialEvent() {
    char inChar = (char)Serial.read();
    switch (inChar) {
      case '8':
        if (state1 == 0){
          state1 = 1;
          }
          else {
          state1 = 0;
          }
        digitalWrite(led1, state1);
        break;
      case '7':
        if (state2 == 0){
          state2 = 1;
          }
          else {
          state2 = 0;
          }
        digitalWrite(led2, state2);
        break;
      case '6':
        if (state3 == 0){
          state3 = 1;
          }
          else {
          state3 = 0;
          }
        digitalWrite(led3, state3);
        break;
      case '5':
        if (state4 == 0){
          state4 = 1;
          }
          else {
          state4 = 0;
          }
        digitalWrite(led4, state4);
        break;
      case '4':
        if (state5 == 0){
          state5 = 1;
          }
          else {
          state5 = 0;
          }
        digitalWrite(led5, state5);
        break;
      case '3':
        if (state6 == 0){
          state6 = 1;
          }
          else {
          state6 = 0;
          }
        digitalWrite(led6, state6);
        break;
      case '2':
        if (state7 == 0){
          state7 = 1;
          }
          else {
          state7 = 0;
          }
        digitalWrite(led7, state7);
        break;      
      default:
        break;
    }
}

