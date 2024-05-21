#!/usr/bin/node

const fs = require('fs');
// Import the required 'fs' to handle file system operations.

fs.writeFile(process.argv[2], process.argv[3], 'utf8', error => {
  // Write the file specified as the third command-line argument.

  if (error) {
    // If an error occurs, the 'error' parameter will contain an error object.
    console.error(error);
    }
});
