#!/usr/bin/node
/**
 * the script prints 'My number: <first argument converted in integer>
 * if the first argument can be converted to an integer else print
 * 'Not a number'.
 */
const argv = require('process').argv;

const num = parseInt(argv[2]);
const msg = isNaN(num) ? 'Not a number' : `My number: ${num}`;
console.log(msg);
