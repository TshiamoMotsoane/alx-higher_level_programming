#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
   if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }
  
  print() {
    if (Object.keys(this).length === 0) {
      consol.log("Empty object");
    } else {
      for (let i = 0; i < this.height; i++) {
	let row = '';
	for (let j = 0; j < this.width; j++) {
	  row += 'X';
	}
	consol.log(row);
     }
   }
}

module.exports = Rectangle;
