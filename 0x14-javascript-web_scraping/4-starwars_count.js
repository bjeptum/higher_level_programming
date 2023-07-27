#!/usr/bin/node
/*
Prints the number of movies
where the character “Wedge Antilles” is present
*/
const request = require('request');
const url = process.argv[2];
const count = 0;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }
  if (response.statusCode === 200) {
    // Parse the response body as JSON
    const filmsData = JSON.parse(body).results;
	// Check for  Wedge Antilles
	for (const film of filmsData) {
		const characters = film.characters;
		for (const character in characters) {
			if (character.endsWith('/18/')) {
				count = count + 1;
			}
		}
	}
	  console.log(count);
  }
});
