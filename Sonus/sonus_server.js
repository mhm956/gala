'use strict';

let net = require('net');
let server = net.createServer(function(socket){
    socket.write('Echo server\r\n')
});

server.listen(5786, '127.0.0.1');

const ROOT_DIR = __dirname + '/node_modules/sonus/';
const Sonus = require(ROOT_DIR + 'index.js');
const speech = require('@google-cloud/speech')({
    projectId: 'streaming-speech-sample',
    keyFilename: __dirname + '/keyfile.json'
});
const hotwords = [{file: ROOT_DIR + 'resources/sonus.pmdl', hotword: 'sonus'}];
const language = "en-US";
const sonus = Sonus.init({hotwords, language, recordProgram: "rec"}, speech);

// Start sonus to listen for the spoken hotword:
Sonus.start(sonus);
console.log('Say "' + hotwords[0].hotword + '"...');

// Waits till hotword is spoken
sonus.on('hotword', (index, keyword) => console.log("!" + keyword));

// When google passes partial result:
sonus.on('partial-result', result => console.log("Partial", result));

// When google passes full result:
sonus.on('final-result', result => {
    server.write(result);
    console.log("Final", result);
    if (result.includes("stop")) {
        Sonus.stop()
    }
});