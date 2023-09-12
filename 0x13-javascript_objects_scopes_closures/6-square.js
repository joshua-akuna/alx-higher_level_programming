#!/usr/bin/node
/**
 * The script defines the Square class
 */
const SuperSquare = require('./5-square');

class Square extends SuperSquare {
  constructor (size) {
    super(size);
    this.size = size;
  }

  charPrint (c) {
    const ch = c || 'X';

    for (let i = 0; i < this.height; i++) {
      let line = '';
      for (let j = 0; j < this.width; j++) {
        line += ch;
      }
      console.log(line);
    }
  }
}

module.exports = Square;
