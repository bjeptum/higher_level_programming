#!/usr/bin/node
// Prints a square
const process = require('process');
const args = process.argv;
const size = parseInt(args[2]);
if (isNaN(size)) {
  console.log('Missing size');
} else {
  let i = 0;

  if (size > 0) {
    for (i = 0; i < size; i++) {
      console.log('X'.repeat(size));
    }
  } else {
    console.log('\n');
  }
}
