#!/usr/bin/node
const dict = require('./101-data').dict;

const newDict = {};

for (let key in dict) {
	val = dict[key];
	if (!(val in newDict)) {
		newDict[val] = [];
	}
	newDict[val].push(key);
}
console.log(newDict);
