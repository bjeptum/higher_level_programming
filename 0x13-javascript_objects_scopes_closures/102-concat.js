#!/usr/bin/node
/*
Concats files
*/
const fs = require('fs');
const myArgs = process.argv;
const arg1 = myArgs[2];
const arg2 = myArgs[3];
const arg3 = myArgs[4];

const File1 = fs.readFileSync(arg1, 'utf8');
const File2 = fs.readFileSync(arg2, 'utf8');

const mergeFiles = File1 + File2;

fs.writeFileSync(arg3, mergeFiles);
