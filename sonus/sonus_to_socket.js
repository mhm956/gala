'use strict';

let endOfLine = require('os').EOL;

let net = require('net-socket');
let socket = net.connect(9999, 'localhost');
const ROOT_DIR = __dirname + '/node_modules/sonus/';

const Sonus = require(ROOT_DIR + 'index.js');
const speech = require('@google-cloud/speech')({
    projectId: 'streaming-speech-sample',
    keyFilename: ROOT_DIR + 'keyfile.json'
});
const hotwords = [{file: ROOT_DIR + 'resources/sonus.pmdl', hotword: 'sonus'}];

const language = "en-US";
//recordProgram can also be 'arecord' which works much better on the Pi and low power devices
const sonus = Sonus.init({hotwords, language, recordProgram: "rec"}, speech);

// Set and turn on the net socket.
socket.setEncoding('utf8');
socket.on('connect', function () {
    // socket.write('SONOS');
});

// // On data coming back to the sonus socket, trigger sonus.trigger()
// socket.on('data', function (data) {
//     sonus.trigger()
// });

// Start sonus to listen for the spoken hotword:
Sonus.start(sonus);

console.log('Say "' + hotwords[0].hotword + '"...');
sonus.on('hotword', (index, keyword) => console.log("!" + keyword));

// When google passes partial result:
sonus.on('partial-result', result => console.log("Partial", result));

// When google passes full result:
sonus.on('final-result', result => {
    socket.write(result);
    console.log("Final", result);
    if (result.includes("stop")) {
        socket.end('Exiting Instance');
        socket.destroy();
        Sonus.stop()
    }
});