#include <Arduino.h>

void setup()
{
  Serial.begin(9600);
}
const int maxMsgCount = 50;
char incomingChar = 0;
char message[maxMsgCount] = {'\0'};
int msgCount = 0;

enum SerialStates
{
  Idle,
  Receiving,
  MessageReceived,
  SendResponse
};
SerialStates serialState = Idle;
void loop()
{
  switch (serialState)
  {
  case Idle:
  {
    if (Serial.available() > 0)
    {
      incomingChar = Serial.read();
      if (incomingChar == '#')
      {
        serialState = Receiving;
      }
    }
  }
  case Receiving:
  {
    incomingChar = Serial.read();
    if (incomingChar != '%' || msgCount >= maxMsgCount)
    {
      message[msgCount] = incomingChar;
      msgCount++;
    }
    else
    {
      msgCount = 0;
      serialState = MessageReceived;
    }
  }
  break;
  case MessageReceived:
  {
    //parse message and move servo

    serialState = SendResponse;
  }
  break;
  case SendResponse:
  {
    //get distance at degree
    serialState = Idle;
  }
  }
}

// {

// Serial.print(incomingByte);
