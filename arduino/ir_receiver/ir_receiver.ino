#include <IRremote.hpp>
#define IR_RECEIVE_PIN 2
#define DECODE_NEC

void setup() {
  Serial.begin(9600);
  IrReceiver.begin(IR_RECEIVE_PIN);

}

void loop() {
  if (IrReceiver.decode()) {

      IrReceiver.resume();

      switch(IrReceiver.decodedIRData.command) {
        case 0x45:
          Serial.println("CH-");
          break;
        case 0x46:
          Serial.println("CH");
          break;
        case 0x47:
          Serial.println("CH+");
          break;
        case 0x44:
          Serial.println("VOL-");
          break;
        case 0x40:
          Serial.println("VOL+");
          break;
        case 0x43:
          Serial.println("PLAY");
          break;
        case 0x7:
          Serial.println("-");
          break;
        case 0x15:
          Serial.println("+");
          break;
        case 0x9:
          Serial.println("EQ");
          break;
        case 0x16:
          Serial.println("0");
          break;
        case 0x19:
          Serial.println("100+");
          break;
        case 0xD:
          Serial.println("200+");
          break;
        case 0xC:
          Serial.println("1");
          break;
        case 0x18:
          Serial.println("2");  
        break;
        case 0x5E:
          Serial.println("3");
          break;
        case 0x8:
          Serial.println("4");
          break;
        case 0x1C:
          Serial.println("5");
          break;
        case 0x5A:
          Serial.println("6");
          break;
        case 0x42:
          Serial.println("7");
          break;
        case 0x52:
          Serial.println("8");
          break;
        case 0x4A:
          Serial.println("9");
          break;
      }
  }
}