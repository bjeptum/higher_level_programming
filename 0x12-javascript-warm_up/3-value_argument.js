#!/usr/bin/node
// Prints the first argument passed to it
// Import process module
const process = require('process');
const args = process.argv;
let len = 0;

// Calculate length of argv array
args.forEach((item) => {
  len++;
});

if (len <= 2) {
  console.log('No argument');
} else {
  console.log(args[2]);
}
