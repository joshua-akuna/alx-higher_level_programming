#!/usr/bin/node
/**
 * The script searches for the second largest integer in a list of arguments
 */
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const newArray = process.argv
	.map(Number)
	.slice(2, process.argv.length)
	.sort((a, b) => a - b)
  console.log(newArray[newArray.length - 2]);
}
