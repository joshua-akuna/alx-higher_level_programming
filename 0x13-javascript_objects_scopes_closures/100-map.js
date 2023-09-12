#!/usr/bin/node

const list = require('./100-data').list
console.log(list);
newList = list.map((val, index) => val * index);
console.log(newList);
