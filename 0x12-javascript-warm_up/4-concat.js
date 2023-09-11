#!/usr/bin/node

/**
 * the script prints two arguments passed to it in the
 * following format: arg1 is arg2.
 */
const argv = require('process').argv;
console.log(`${argv[2]} is ${argv[3]}`);
