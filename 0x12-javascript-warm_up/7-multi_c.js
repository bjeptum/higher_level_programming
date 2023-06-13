#!/usr/bin/node
// Prints x times C is fun
const process = require('process');
const args = process.argv;
const x = parseInt(args[2]);
if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  let j = 0;
  while (j < x) {
    console.log('C is fun');
    j++;
  }
}
