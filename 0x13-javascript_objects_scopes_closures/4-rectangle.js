#!/usr/bin/node
/**
 * The script defines a Rectangle class
 */
class Rectangle {
	constructor(w, h) {
		if (w > 0 && h > 0)
		{
			this.width = w;
			this.height = h;
		}
	}

	print() {
		for (let i = 0; i < this.height; i++) {
			let line = '';
			for (let j = 0; j < this.width; j++) {
				line += 'X';
			}
			console.log(line);
		}
	}

	rotate() {
		let temp = this.width;
		this.width = this.height;
		this.height = temp;
	}

	double() {
		this.width *= 2;
		this.height *= 2;
	}
}

module.exports = Rectangle;
