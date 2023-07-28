#!/usr/bin/node
/*
Prints all characters of a Star Wars movie
*/
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films';
const movieId = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }
  if (response.statusCode === 200) {
    // Parse the response body as JSON
    const filmsData = JSON.parse(body).results;

    // Find movie with the given id
    const movie = filmsData.find(film => film.episode_id === parseInt(movieId));
    if (!movie) {
      console.log('Movie not found.');
      process.exit(1);
    }

    // Print characters from the movie
	const characters = movie.characters;
	const promises = characters.map(characterUrl => {
		return new Promise((resolve, reject) => {
			request(characterUrl, (charError, charResponse, charBody) => {
				if (charError) {
					reject(charError);
					return;
				}
			if (charResponse.statusCode === 200) {
				const character = JSON.parse(charBody);
				resolve(character.name);
			}
			});
		});
	});
    
    Promise.all(promises)
      .then(names => {
		  names.forEach(name => console.log(name));
      })
      .catch(error => {
        console.error(error);
      });
  }
});
