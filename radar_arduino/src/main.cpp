#include <Arduino.h>
#include "definitions.h"
#include "ultrasone.h"
#include <Servo.h>
Servo myservo;

void setup()
{
	Serial.begin(9600);

	// sensor
	pinMode(TrigPin, OUTPUT);
	pinMode(EchoPin, INPUT);
	pinMode(Piezo, OUTPUT);
	myservo.attach(ServoPin);
}
//incomingmessage
char incomingChar = 0;
char message[MaxMsgCount] = {'\0'};
int msgCount = 0;

//sensor
float distance = 100;

//servo
int degree = 0;
States state = ProcessingData;

void loop()
{

	switch (state)
	{
	case ProcessingData:
	{
		delay(100);
		distance = getDistance();
		degree++;
		if (degree > 360)
		{
			degree = 0;
		}
		if (distance > 70)
		{
			distance = -1;
			// analogWrite(Piezo, 200);
		}else{
			// analogWrite(Piezo, 0);
		}
		
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
