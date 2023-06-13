#!/usr/bin/node
// Prints the addition of 2 integers
const process = require('process');
const args = process.argv;
const n1 = parseInt(args[2]);
const n2 = parseInt(args[3]);
function add (a, b) {
  const addition = a + b;
  return (addition);
}
console.log(add(n1, n2));
