#!/usr/bin/node

// Import the required 'fs' module to handle file system operations.
const fs = require('fs');

// Read the file specified by the first command-line argument.
fs.readFile(process.argv[2], 'utf8', function (err, data) {

  //If an error occurs, log it to the console.
  if (err) {
    console.error('Error reading the file:', err);
  } else {
    // If no error, print the file content to the console.
    console.log(data);
  }
});
