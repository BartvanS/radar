const express = require('express')
const app = express()
const appPort = 3000
const path = require('path')
const http = require('http').createServer(app)
const io = require('socket.io')(http)
// const Serial = require('./modules/serial')

app.use(express.static('public'))
app.get('/', (req, res) => {
  res.sendFile(path.resolve('public/posenet.html'))
})
http.listen(appPort, () => {
  console.log(`local server: http://localhost:${appPort}`)
})
//sockets

io.on('connection', socket => {
  socket.on('frontcam', msg => {
   
  })
  socket.on('disconnect', reason => {})
})



const Readline = require("@serialport/parser-readline");
const SerialPort = require("serialport");
const port = new SerialPort("com8");

port.write("main screen turn on", function (err) {
  if (err) {
    return console.log("Error on write: ", err.message);
  }
  console.log("message written");
});

// Open errors will be emitted as an error event
port.on("error", function (err) {
  console.log("Error: ", err.message);
});

const parser = port.pipe(new Readline())
parser.on('data', console.log)