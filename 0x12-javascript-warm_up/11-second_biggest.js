#!/usr/bin/node
/*
 Searches the second biggest integer in the list of arguments
 Assume all arguments can be converted to integer
 If no argument passed, print 0
 If the number of arguments is 1, print 0
 */
const process = require('process');

function secondLargest (args) {
  if (args.length < 2) {
    return 0;
  }
  let largest = -Infinity;
  let secondLargest = -Infinity;
  for (let i = 0; i < args.length; i++) {
    const num = parseInt(args[i]);
    if (num > largest) {
      secondLargest = largest;
      largest = num;
    } else if (num > secondLargest && num < largest) {
      secondLargest = num;
    }
  }
  return secondLargest;
}

const args = process.argv.slice(2);
console.log(secondLargest(args));
