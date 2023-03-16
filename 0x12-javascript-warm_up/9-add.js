#!/usr/bin/node
// Prints the addition of two integers
const process = require('process');

function add (a, b) {
  const sum = a + b;
  return (sum);
}

const num1 = parseInt(process.argv[2]);
const num2 = parseInt(process.argv[3]);
console.log(add(num1, num2));
