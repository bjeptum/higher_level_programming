#!/usr/bin/node
// Prints the addition of two integers
const process = require('process');
const args = process.argv;
const a  = parseInt(args[2]);
const b = parseInt(args[3]);

function add(a, b) {
	let result = a + b;
	return result;
}
