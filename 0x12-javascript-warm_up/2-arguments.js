#!/usr/bin/node
// Prints a message depending of the number of arguments passed
const process = require('process');
const args = process.argv;
if (args.length === 0) { console.log('No argument'); } else if (args.length === 1) { console.log('Argument found'); } else { console.log('Arguments found'); }
