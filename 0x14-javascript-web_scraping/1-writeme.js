#!/usr/bin/node
/*
Writes a string to a file
 */
const fs = require('fs');
const file = process.argv[2];
const newString = process.argv[3];

fs.writeFile(file, newString, 'utf-8', function (err, data) {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
