#!/usr/bin/node
/*
 Defines a Rectangle
 If w or h is equal to 0 or not a positive integer
 create an empty object
*/
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || !Number.isInteger(w) || h <= 0 || !Number.isInteger(h)) {
      return {};
    }
    this.width = w;
    this.height = h;
  }
}
module.exports = Rectangle;
