#!/usr/bin/node
// Prints two arguments passed to it
// Import process module
const process = require('process');
const args = process.argv;
let len = 0;

// Calculate length of argv array
args.forEach((item) => {
  len++;
});

if (len <= 4) {
  console.log(args[2] + ' ' + 'is' + ' ' + args[3]);
}
