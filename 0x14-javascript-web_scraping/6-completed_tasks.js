#!/usr/bin/node
/*
 * The script computes the number of tasks completed by the id.
 *   - the first argument is the API URL
 *   - only print users with completed task
 *   - must use the module request
 */

const request = require('request');

if (process.argv.length === 3) {
  request(process.argv[2], (err, response, body) => {
    if (err) {
      console.log(err);
      return;
    }
    const tasks = JSON.parse(body);
    console.log(tasks);
    const map = {};
    for (const task of tasks) {
      if (task.completed) {
        const userId = task.userId;
        map[userId] = map[userId] === undefined ? 1 : parseInt(map[userId]) + 1;
      }
    }
    console.log(map);
  });
}
