#!/usr/bin/node
/*
 concats 2 files
 The first argument is the file path of the first source file
 The second argument is the file path of the second source file
 The third argument is the file path of the destination
*/
const fs = require('fs');

const sourceFile1 = process.argv[2];
const sourceFile2 = process.argv[3];
const destinationFile = process.argv[4];

const data1 = fs.readFileSync(sourceFile1, 'utf8');
const data2 = fs.readFileSync(sourceFile2, 'utf8');

const concatenatedData = data1 + data2;

fs.writeFileSync(destinationFile, concatenatedData);
