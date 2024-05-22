#!/usr/bin/node

const request = require('request');

// Construct the URL using the provided episode number
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

// Make a GET request to the URL
request(url, function (error, response, body) {
  if (error) {
  console.error('Error:', error);
  } else {

  // Parse the response body and print the title of the film
  console.log(JSON.parse(body).title);
  }
});
