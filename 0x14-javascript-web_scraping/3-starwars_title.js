#!/usr/bin/node
/*
Prints the title of a Star Wars movie
where the episode number matches a given integer
*/
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
const movieID = process.argv[2];

if (!movieID) {
  console.error('Please provide a movie ID as an argument.');
  process.exit(1);
}

request(url + movieID, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }
  if (response.statusCode === 200) {
    // Parse the response body as JSON
    const movieData = JSON.parse(body);
    // Print the title of the movie
    console.log(movieData.title);
  } else {
    console.error('Error:', response.statusCode, response.statusMessage);
    process.exit(1);
  }
});
