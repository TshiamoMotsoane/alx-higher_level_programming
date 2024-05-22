#!/usr/bin/node

const request = require('request');

// Make a GET request to the specified URL
request.get(process.argv[2])

  .on('response', function (response) {

  // Print the status code of the response
  console.log('code:', response.statusCode);
});
