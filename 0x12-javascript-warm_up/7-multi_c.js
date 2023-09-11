#!/usr/bin/node
/**
 * the script prints x times "C is fun"
 */
const argv = require('process').argv;

const msg = 'C is fun';
const num = parseInt(argv[2], 10);
if (isNaN(num)) {
  console.log('Missing number of occurences');
} else {
  for (let x = 0; x < num; x++) { console.log(msg); }
}
