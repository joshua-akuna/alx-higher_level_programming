#!/usr/bin/node
/**
 * The script computes and prints the factorial of a number
 * passed as a commandline argument
 */
const argv = require('process').argv;

const num = parseInt(argv[2], 10);
const input = isNaN(num) ? 1 : num;
const fact = factorial(input);
console.log(fact);

function factorial (arg) {
  if (arg <= 1) { return 1; }
  return arg * factorial(arg - 1);
}
