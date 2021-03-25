#ifndef DEFINITIONS_H
#define DEFINITIONS_H

//protocol
#define MaxMsgCount 50
#define StartByte '#'
#define StopByte '%'
#define Delimiter '|'
//ultrasone sensor
#define TrigPin 9
#define EchoPin 8
#define Piezo 10

//states
enum States
{
  ProcessingData,
  ReceivingMessage,
  ProcessMessage
};
#endif