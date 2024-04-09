#!/usr/bin/node
if (process.argv.length === 2) {
  consol.log('No argument');
} else if (process.argv.length === 3) {
  console.log('Argument fount');
} else {
  console.log('Arguments found');
}
