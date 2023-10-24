#!/usr/bin/node
/*
 * The script displays the status code of a GET request
 *    - The first argument is the URL to request
 *    - The status code must be printed like this: code: <statuscode>
 *    - You must use the module request
 */
const request = require('request');

if (process.argv.length === 3) {
  request(process.argv[2], (err, response, body) => {
    if (err) {
      console.log(err);
      return;
    }
    console.log(`code: ${response && response.statusCode}`);
  });
}
