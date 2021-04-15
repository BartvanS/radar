#include <Arduino.h>
#include "definitions.h"
#include "ultrasone.h"
#include <Servo.h>
Servo myservo;
void setup()
{
	Serial.begin(9600);
	myservo.attach(ServoPin);
	myservo.write(0);
	// sensor pins
	pinMode(TrigPin, OUTPUT);
	pinMode(EchoPin, INPUT);
}
//sensor
float distance = 100;
//servo
int currentDegree = 0;
States state = ProcessingData;
int direction = 1;
int multiplyier = 2;
void loop()
{
		delay(100);
		int newDegree = currentDegree + direction * multiplyier;
		if (newDegree > MAX_DEGREES)
		{
			direction = -1;
		}
		else if (newDegree <= 0)
		{
			direction = 1;
		}
		currentDegree = newDegree;
		myservo.write(currentDegree);
		distance = getDistance();
		Serial.print(currentDegree);
		Serial.print(Delimiter);
		Serial.println((int)distance); //print the distance that was measured



}
