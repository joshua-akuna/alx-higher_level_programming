#!/usr/bin/node
/*
 * The script writes a string to a file
 *   - first argument is the file path
 *   - the second argument is the string to write
 *   - The content of the file mist be written in utf-8
 *   - if an error occurs while writing, print the error object
 */

const fs = require('fs');

if (process.argv.length === 4) {
  try {
    fs.writeFileSync(process.argv[2], process.argv[3], 'utf-8');
  } catch (err) {
    console.log(err);
  }
}
