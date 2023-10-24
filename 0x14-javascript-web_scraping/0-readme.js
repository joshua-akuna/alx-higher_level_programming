#!/usr/bin/node
/*
 * The script reads and prints the content of a file
 *   - The first argument is the file path
 *   - the content of the file must be read in utf-8
 *   - if an error occur during the printing, print the error
 */

const fs = require('fs');

if (process.argv.length === 3) {
  try {
    const data = fs.readFileSync(process.argv[2], 'utf-8');
    console.log(data);
  } catch (err) {
    console.log(err);
  }
}
