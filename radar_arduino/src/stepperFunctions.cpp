#include <Arduino.h>
#include <stepperFunctions.h>
#define MAX_DEGREES 360
float stepInDegrees(int degree, int *currentDegree)
{
      int newDegree = *currentDegree += degree;
      if (newDegree > MAX_DEGREES)
      {
            *currentDegree = newDegree - MAX_DEGREES;
      }
      else
      {
            *currentDegree = newDegree;
      }
      
}