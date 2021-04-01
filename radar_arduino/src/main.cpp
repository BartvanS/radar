#include <Arduino.h>
#include "definitions.h"
#include "ultrasone.h"
// #include <Stepper.h>
#include <Servo.h>
// #include "stepperFunctions.h"
// Stepper stepper(STEPS, 8, 10, 9, 11);
Servo myservo;
void setup()
{
  Serial.begin(9600);
//   stepper.setSpeed(1); // 1 rpm
myservo.attach(ServoPin);
myservo.write(0);
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
#define MAX_DEGREES 180
int direction = 1;
int multiplyier = 2;
void loop()
{
  switch (state)
  {
  case ProcessingData:
  {
	  delay(100);
	int newDegree = currentDegree + direction * multiplyier;
      if (newDegree > MAX_DEGREES)
      {
            direction = -1;
      }
      else if(newDegree <= 0)
      {
            direction = 1;
      }
	  currentDegree = newDegree;
    myservo.write(currentDegree); 
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
