#!/usr/bin/node
/*
Defines Square class inherits from Square1
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
      let str = '';
      for (let i = 0; i < this.width; i++) {
        str += c;
      }
      for (let i = 0; i < this.height; i++) {
        console.log(str);
      }
    }
  }
}
module.exports = Square;
