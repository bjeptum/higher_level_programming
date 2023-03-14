#!/usr/bin/node
/* Prints C is fun x times
 * x is first argument(integer) passed
 */
const process = require('process');
const args = process.argv;
const num = parseInt(args[2]);
if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  while (i < num) {
    console.log('C is fun');
    i++;
  }
}
