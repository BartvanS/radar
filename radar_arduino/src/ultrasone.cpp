#include "ultrasone.h"
#include <Arduino.h>
float getDistance()
{
  float echoTime;           //variable to store the time it takes for a ping to bounce off an object
  float calculatedDistance = -1; //variable to store the distance calculated from the echo time

  //send out an ultrasonic pulse that's 10ms long
  digitalWrite(TrigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(TrigPin, LOW);

  echoTime = pulseIn(EchoPin, HIGH); //use the pulsein command to see how long it takes for the
                                     //pulse to bounce back to the sensor

  calculatedDistance = echoTime / 58.0; //calculate the distance of the object that reflected the pulse (half the bounce time multiplied by the speed of sound)

  return calculatedDistance; //send back the distance that was calculated
}