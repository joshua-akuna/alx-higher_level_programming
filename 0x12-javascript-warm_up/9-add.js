#!/usr/bin/node
/**
 * the script prints the addition of 2 integers
 */
const argv = require('process').argv;
const num1 = parseInt(argv[2]);
const num2 = parseInt(argv[3]);

if (!isNaN(num1) && !isNaN(num2)) { console.log(add(num1, num2)); }

function add (a, b) {
  return a + b;
}
