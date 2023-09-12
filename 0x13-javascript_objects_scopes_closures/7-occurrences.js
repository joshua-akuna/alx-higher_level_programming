#!/usr/bin/node

exports.nbOccurrences = function (list, searchElement) {
	let mode = 0;
	for (let item of list) {
		if (item === searchElement) { mode++ }
	}
	return mode;
};
