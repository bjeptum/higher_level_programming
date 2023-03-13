#!/usr/bin/node
// Prints a message depending of the number of arguments passed
const process = require('process');
const args = process.argv.slice(2);
if (args.length === 0) {
  console.log('No argument');
} else if (args.length === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
