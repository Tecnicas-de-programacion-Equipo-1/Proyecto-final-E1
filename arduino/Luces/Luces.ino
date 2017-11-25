int led1 = 8;
int led2 = 7;
int led3 = 6;
int led4 = 5;
int led5 = 4;
int led6 = 3;
int led7 = 2;
int state = 0;

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
    String inString = (String)Serial.readString();
    char inChar = char(inString[inString.length()-1]);
    state = int(inString[0]);
    switch (inChar) {
      case 'F':
        digitalWrite(led1, state);
        break;
      case 'C':
        digitalWrite(led2, state);
        break;
      case 'A':
        digitalWrite(led3, state);
        break;
      case 'B':
        digitalWrite(led4, state);
        break;
      case 'E':
        digitalWrite(led5, state);
        break;
      case 'G':
        digitalWrite(led6, state);
        break;
      case 'D':
        digitalWrite(led7, state);
        break;      
      case 'H':
        state = 0;
        digitalWrite(led1, state);
        digitalWrite(led2, state);
        digitalWrite(led3, state);
        digitalWrite(led4, state);
        digitalWrite(led5, state);
        digitalWrite(led6, state);
        digitalWrite(led7, state);
        break;      
      default:
        break;
    }
}

