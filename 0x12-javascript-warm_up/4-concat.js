#!/usr/bin/node
// Prints out a sentence
const process = require('process');
const myArgs = process.argv;
// Calculate length of arguments
let len = 0;
myArgs.forEach((item) => {
  len++;
});
if (len <= 4) {
  console.log(myArgs[2] + ' ' + 'is' + ' ' + myArgs[3]);
}
