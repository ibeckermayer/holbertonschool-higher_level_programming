#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (typeof (w) === 'undefined' || typeof (h) === 'undefined' || w <= 0 || h <= 0) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}
module.exports = Rectangle;
