#!/usr/bin/node
/*
Gets the contents of a webpage and
Stores it in a file
*/
const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  if (response.statusCode !== 200) {
    console.error('Failed to fetch the webpage. Status code:', response.statusCode);
    return;
  }
  fs.writeFile(filePath, body, { encoding: 'utf8' }, (err) => {
    if (err) {
      console.error(err);
    }
  });
});
