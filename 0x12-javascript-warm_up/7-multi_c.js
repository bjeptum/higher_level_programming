#!/usr/bin/node
/* Prints C is fun x times
 * x is first argument(integer) passed
 */
const process = require('process');
const args = process.argv;
const num = parseInt(args[2]);
for ( let i = 0; i < num; i++) {
  console.log('C is fun' * i);
} else {
  console.log('Missing number of occurrences');
}
