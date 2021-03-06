#ifndef DEFINITIONS_H
#define DEFINITIONS_H

//protocol
#define MaxMsgCount 50
#define StartByte '#'
#define StopByte '%'
#define Delimiter '|'
//ultrasone sensor
#define TrigPin 8
#define EchoPin 9
#define Piezo 10
//servo
#define ServoPin 6
#define MAX_DEGREES 180

//states
enum States
{
  ProcessingData,
  ReceivingMessage,
  ProcessMessage
};
#endif