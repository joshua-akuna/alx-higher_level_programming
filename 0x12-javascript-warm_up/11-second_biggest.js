#!/usr/bin/node
/**
 * The script searches for the second largest integer in a list of arguments
 */
const argv = require('process').argv;

const newArray = [];
for (let i = 2; i < argv.length; i++) {
  newArray.push(parseInt(argv[i]));
}

newArray.sort().reverse();
console.log(newArray[1] ? newArray[1] : 0);
