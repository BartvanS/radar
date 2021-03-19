#include <Arduino.h>

void setup()
{
  Serial.begin(9600);
}
char incomingByte = 0;
void loop()
{
  String message 
  if (Serial.available() > 0)
  {
    incomingByte = Serial.read();
    Serial.print(incomingByte);
  }
}