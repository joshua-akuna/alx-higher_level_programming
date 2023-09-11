#!/usr/bin/node
/*
 * the script prints a message depending on the number of arguments passed
 */

const process = require('process');

const argvLen = process.argv.length;
const msg = argvLen === 2
  ? 'No argument'
  : argvLen === 3 ? 'Argument found' : 'Arguments found';
console.log(msg);
