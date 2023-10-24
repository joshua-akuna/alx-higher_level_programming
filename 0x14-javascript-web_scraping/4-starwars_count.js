#!/usr/bin/node
/*
 * The script prints the number of moveis where the character
 *    "Wedge Antilles" is present
 *    - Wedge Antilles is character ID 18 - your script must use
 *       this ID for filtering the result of the API
 *    - You must use the module request
 */

const request = require('request');

if (process.argv.length === 3) {
  const WEDGE_ID = 18;
  request(process.argv[2], (err, response, body) => {
    if (err) {
      console.log(err);
      return;
    }

    let count = 0;
    const jsonData = JSON.parse(body);
    for (const result of jsonData.results) {
      const characters = result.characters;
      for (const character of characters) {
        if (character.includes(WEDGE_ID)) {
          count++;
          break;
        }
      }
    }
    console.log(count);
  });
}
