#include <Arduino.h>
#include "definitions.h"
#include "ultrasone.h"
void setup()
{
  Serial.begin(9600);

  // sensor
  pinMode(TrigPin, OUTPUT);
  pinMode(EchoPin, INPUT);
}
//incomingmessage
char incomingChar = 0;
char message[MaxMsgCount] = {'\0'};
int msgCount = 0;

//sensor
float distance = 0;

//servo
int degree = 0;
States state = ProcessingData;

void loop()
{

  switch (state)
  {
  case ProcessingData:
  {
    distance = getDistance();
    Serial.print(degree);
    Serial.print(Delimiter);
    Serial.println((int)distance); //print the distance that was measured
    // checkSerialIn();
  }
  break;

    // case ReceivingMessage:
    // {
    //   incomingChar = Serial.read();
    //   if (incomingChar != StopByte)
    //   {
    //   }
    //   else
    //   {
    //     state = ProcessMessage;
    //   }
    // }
    // break;

    // case ProcessMessage:
    // {
    //   state = ProcessingData;
    // }
    // break;
  }
}
