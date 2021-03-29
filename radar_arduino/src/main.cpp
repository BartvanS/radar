#include <Arduino.h>
#include "definitions.h"
#include "ultrasone.h"
#include <Stepper.h>
#include "stepperFunctions.h"
Stepper stepper(STEPS, 8, 10, 9, 11);

void setup()
{
  Serial.begin(9600);
  stepper.setSpeed(1); // 1 rpm
  // sensor
  pinMode(TrigPin, OUTPUT);
  pinMode(EchoPin, INPUT);
}
//incomingmessage
char incomingChar = 0;
char message[MaxMsgCount] = {'\0'};
int msgCount = 0;

//sensor
float distance = 100;

//servo
int currentDegree = 0;
States state = ProcessingData;

void loop()
{
  switch (state)
  {
  case ProcessingData:
  {
    // stepper.step(2038);
    
    distance = getDistance();
    Serial.print(currentDegree);
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
