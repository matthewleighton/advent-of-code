const fs = require('fs');

// class Utils {
// 	getData() {
// 		fs.readFile('data.txt', 'utf8', (err, data) => {
// 			if (err) {
// 				console.log(err)
// 			}

// 			return data
// 		});
// 	}
// }

function getData() {
	// fs.readFile('data.txt', 'utf8', (err, data) => {
	// 	if (err) {
	// 		console.log(err)
	// 	}

	// 	return data
	// });

	return fs.readFileSync('data.txt', 'utf8');
}

module.exports.getData = getData