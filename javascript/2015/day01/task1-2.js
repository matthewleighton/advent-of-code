const helper = require('./helper');
const utils = require('../../utils');
var data = utils.getData()[0];

function handleCharacter(char) {
	if (char == '(') return 1;

	return -1;
}

var floor = 0;
var entered_basement = false;

for (var i = 0; i < data.length; i++) {
	floor += handleCharacter(data[i]);

	if (floor == -1 && entered_basement === false) {
		entered_basement = i+1;
	}

}

console.log('Task 1:', floor);
console.log('Task 2:', entered_basement);