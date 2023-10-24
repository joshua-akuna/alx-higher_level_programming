#!/usr/bin/node
/*
 * The script gets the contents of a web page and stores it in a file
 *    - The first argument is the URL to request
 *    - The second argument is the file path to store the body response
 *    - The file must be UTF-8 encoded
 *    - You must use the module request
 */

const request = require('request');
const fs = require('fs');

if (process.argv.length === 4) {
  request(process.argv[2], (err, response, body) => {
    if (err) {
      console.log(err);
      return;
    }

    try {
      fs.writeFileSync(process.argv[3], body, 'utf-8');
    } catch (error) {
      console.log(error);
    }
  });
}
