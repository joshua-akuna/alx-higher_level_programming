#!/usr/bin/node
/*
 * The script prints the title of a Star wars movie where the
 *    episode number matches a given integer.
 *    - The first argument is the movie ID
 *    - You must use the module request
 */

const request = require('request');

if (process.argv.length === 3) {
  const URL = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
  request(URL, (err, response, body) => {
    if (err) {
      console.log(err);
      return;
    }
    const jsonData = JSON.parse(body);
    console.log(jsonData.title);
  });
}
