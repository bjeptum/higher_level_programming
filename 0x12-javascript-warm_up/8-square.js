#!/usr/bin/node
// Prints a square
const process = require('process');
const args = process.argv;
const x = parseInt(args[2]);
if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  let str = '';
  for (let i = 0; i < x; i++) {
    for (let j = 0; j < x; j++) {
      str += 'X';
    }
    if (i !== x - 1) {
      str += '\n';
    }
  }
  console.log(str);
}
