#!/usr/bin/node
const fs = require('fs');

try{
	let content = '';
	content += fs.readFileSync(`./${process.argv[2]}`, 'utf8');
	content += fs.readFileSync(`./${process.argv[3]}`, 'utf8');
	fs.writeFileSync(`./${process.argv[4]}`, content);
} catch (err) {
	console.error(err);
}
