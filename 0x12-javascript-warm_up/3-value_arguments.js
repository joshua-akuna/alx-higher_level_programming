#!/usr/bin/node
/**
 * the script prints the first argument passed to it.
 */

const argv = require('process').argv;
const msg = argv[2] ? argv[2] : 'No argument';
console.log(msg);
