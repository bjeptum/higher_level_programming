#!/usr/bin/node
// Prints first script if it can be converted to integer
const process = require('process');
const myArgs = process.argv;
const value = parseInt(myArgs[2]);
if (value) {
  console.log('My number:' + ' ' + value);
} else {
  console.log('Not a number');
}
