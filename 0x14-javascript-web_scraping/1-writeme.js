#!/usr/bin/node

const fs = require('fs');

// Check if the correct number of arguments is provided
if (process.argv.length < 4) {
    console.error('Usage: ./script.js <file_path> <string_to_write>');
    process.exit(1); // Exit the script with a failure code.
}

//Extract the file path and the string to write from the command line arguments
const filePath = process.argv[2];
const stringToWrite = process.argv[3];

// Write the string to the specified file in the UTF-8 encoding
fs.writeFile(filePath, stringToWrite, 'utf8', function (err) {
    // If an eror occurs, log it to the console
    if (err) {
	console.error('Error writing to the file:', err);
    } else {
	console.log('File written successfully');
    }
});
