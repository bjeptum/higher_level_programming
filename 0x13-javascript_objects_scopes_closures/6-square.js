#!/usr/bin/node
/*
 Defines a square and inherits from Rectangle
 Instance method charPrint(c) prints the rectangle using the character c
 If c is undefined, use the character X
*/
const Square1 = require('./5-square');

class Square extends Square1 {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (!c) {
      super.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log('c'.repeat(this.width));
      }
    }
  }
}
module.exports = Square;
