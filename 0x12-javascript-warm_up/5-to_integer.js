#!/usr/bin/node
/* Prints sentence if
 * the first argument can be converted to an integer
 */
const process = require('process');
const args = process.argv;
const num = parseInt(args[2]);
if (num) {
  console.log('My number:' + ' ' + num);
} else {
  console.log('Not a number');
}
