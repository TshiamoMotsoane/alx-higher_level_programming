#!/usr/bin/node
const Square = require('.5-square');

class Square extends Square {
	charPrint (c) {
		if (c === undefined) {
			c = 'X';
		}
		for (let i = 0; i < this.height; i++) {
			let row = '';
			for (let j = 0; j < this.width; j++) {
				row += c;
			}
			console.log(row);
		}
	}
}

module.exports = Square;
