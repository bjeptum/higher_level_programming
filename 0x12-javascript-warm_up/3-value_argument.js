#!/usr/bin/node
// Prints first argument passed
const process = require('process');
const myArgs = process.argv;
let len = 0;
myArgs.forEach((item) => {
	len++;
});
if (len <= 2) {
	console.log('No argument');
} else {
	console.log(myArgs[2]);
}
