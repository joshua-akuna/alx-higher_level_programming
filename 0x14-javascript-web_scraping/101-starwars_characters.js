#!/usr/bin/node
/**
 * The script prints all characters of a Star Wars movie:
 *    - The first argument is the Movie ID - example: 3 = "Return of the Jedi"
 *    - Display one character name by line in the same order of the list
 *       "characters" in the /films/ response
 *    - You must use the StartWars API
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

    const data = JSON.parse(body);
    const characters = data.characters;

    for (const character of characters) {
      request(character, (err, response, body) => {
        if (err) {
          console.log(err);
          return;
        }
        const actor = JSON.parse(body);
        console.log(actor.name);
      });
    }
  });
}
