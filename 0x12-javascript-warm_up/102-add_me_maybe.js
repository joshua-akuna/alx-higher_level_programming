#!/usr/bin/node
/**
 * The script increments the number argument and
 * calls the function.
 */
exports.addMeMaybe = function (number, theFunction) {
  theFunction(++number);
};
