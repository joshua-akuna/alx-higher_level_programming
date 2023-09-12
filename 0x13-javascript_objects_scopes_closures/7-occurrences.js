#!/usr/bin/node

exports.nbOccurrences = function (list, searchElement) {
	const occurrences = list.filter((item)=> item === searchElement);
	return occurrences.length;
}
