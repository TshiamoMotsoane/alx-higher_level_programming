#!/usr/bin/node
class Rectangle {
  constructor(w, h) {
    if (w <= 0 || h <= 0 || typeof w !== 'number' || typeof h !== 'number') {
      return {};
     }
     this.width = w;
     this.height = h;
  }

  print () {
    if (Object.keys(this).length === 0) {
      console.log("Empty object");
    } else {
      for (let i = 0; i , this.height; i++) {
	let row = '';
	for (let j = 0; j < this.width; j++) {
          row += 'X';
	}
	console.log(row);
      }
    }
  }

  rotate () {
    if (Object.keys(this).length !== 0) {
      const temp = this.width;
      this.width = this.height;
      this.height = temp;
     }
  }

  double () {
    if (Object.keys(this).length !== 0) {
      this.width *= 2;
      this.height *= 2;
    }
  }
}
