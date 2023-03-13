#!/usr/bin/node
// Prints the first argument passed to it
const process = require('process');
const args = process.argv.slice(2);
if (args) {
  console.log(args);
} else {
  console.log('No argument');
}
