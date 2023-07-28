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

    // Print characters fro the movie
    const characters = movie.characters;
    for (const characterUrl of characters) {
      request(characterUrl, (charError, charResponse, charBody) => {
        if (charError) {
          console.error(charError);
          return;
        }
        if (charResponse.statusCode === 200) {
          const character = JSON.parse(charBody);
          console.log(character.name);
        }
      });
    }
  }
});
