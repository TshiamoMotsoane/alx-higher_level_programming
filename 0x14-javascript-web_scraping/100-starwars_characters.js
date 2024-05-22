#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Fetch the movie details
request(apiUrl, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Error: Invalid status code', response.statusCode);
    return;
  }

  try {
    const movie = JSON.parse(body);
    const characters = movie.characters;

    characters.forEach((characterUrl) => {
      // Fetch each character's details
      request(characterUrl, function (charError, charResponse, charBody) {
        if (charError) {
          console.error('Error:', charError);
          return;
        }

        if (charResponse.statusCode !== 200) {
          console.error('Error: Invalid status code', charResponse.statusCode);
          return;
        }

        try {
          const character = JSON.parse(charBody);
          console.log(character.name);
        } catch (charParseError) {
          console.error('Error parsing character JSON:', charParseError);
        }
      });
    });
  } catch (parseError) {
    console.error('Error parsing movie JSON:', parseError);
  }
});
