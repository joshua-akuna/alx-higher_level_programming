#!/usr/bin/node
/**
 * the script prints a square
 */
const argv = require('process').argv;
const num = parseInt(argv[2], 10);

if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let x = 0; x < num; x++) {
    let str = '';
    for (let y = 0; y < num; y++) {
      str += 'X';
    }
    console.log(str);
  }
}
