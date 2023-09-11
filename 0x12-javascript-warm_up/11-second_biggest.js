#!/usr/bin/node
/**
 * The script searches for the second largest integer in a list of arguments
 */
if (process.argv.length <= 3) {
  console.log('0');
} else {
  const newArray = process.argv.slice(2).map(Number);
  newArray.sort().reverse();
  console.log(newArray[1]);
}
