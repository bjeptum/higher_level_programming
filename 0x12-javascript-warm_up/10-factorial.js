#!/usr/bin/node
// Computes and  prints a factorial
const process = require('process');
const args = process.argv;
const value = parseInt(args[2]);

function factorial (num) {
  if (isNaN(num)) {
    return 1;
  } else if (num === 0) {
    return 1;
  } else {
    return (num * factorial(num - 1));
  }
}
console.log(factorial(value));
