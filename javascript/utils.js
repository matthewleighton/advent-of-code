const fs = require('fs');

function getData() {
	return fs.readFileSync('data.txt', 'utf8').split('\n');
}

module.exports.getData = getData