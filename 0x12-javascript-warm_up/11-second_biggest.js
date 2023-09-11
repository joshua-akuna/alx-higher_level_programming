#!/usr/bin/node
/**
 * The script searches for the second largest integer in a list of arguments
 */
const list = process.argv
  .map(Number)
  .slice(2, process.argv.length)
  .sort((a, b) => a - b)
  .reverse();
console.log(list[1] ? list[1] : 0);
