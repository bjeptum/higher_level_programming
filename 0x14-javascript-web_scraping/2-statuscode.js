#!/usr/bin/node
/*
Display the status code of a GET request
*/
const request = require('request');

const url = process.argv[2];
request(url, (error, response) => {
  if (error) console.log(error);
  const statusCode = response.statusCode;
  console.log(`code: ${statusCode}`);
});
