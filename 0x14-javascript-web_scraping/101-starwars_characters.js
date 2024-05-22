#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Function to fetch character details
function fetchCharacter (characterUrl) {
  return new Promise((resolve, reject) => {
    request(characterUrl, function (error, response, body) {
      if (error) {
        reject(error);
        return;
      }
      if (response.statusCode !== 200) {
        reject(new Error(`Invalid status code: ${response.statusCode}`));
        return;
      }
      const character = JSON.parse(body);
      resolve(character.name);
    });
  });
}

// Fetch movie details
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
    const characterUrls = movie.characters;
    const characterPromises = characterUrls.map(fetchCharacter);

    Promise.all(characterPromises)
      .then(characters => {
        characters.forEach(character => console.log(character));
      })
      .catch(err => {
        console.error('Error fetching character:', err);
      });
  } catch (parseError) {
    console.error('Error parsing movie JSON:', parseError);
  }
});
