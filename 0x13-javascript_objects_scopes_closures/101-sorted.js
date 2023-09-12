#!/usr/bin/node
const dict = require('./101-data').dict;

const newDict = {};

for (const key in dict) {
  const val = dict[key];
  if (!(val in newDict)) {
    newDict[val] = [];
  }
  newDict[val].push(key);
}
console.log(newDict);
