const md5 = require('blueimp-md5');

function checkHash(key, inputValue, n) {
	hash = md5(`${key}${inputValue}`);

	firstCharacters = hash.substring(0, n);

	if (firstCharacters == '0'.repeat(n)) {
		return true;
	} else {
		return false;
	}
}

function solveTask(key, n) {
	inputValue = 1;
	while (true) {
		if (checkHash(key, inputValue, n)) {
			return inputValue
		}

		inputValue++;
	}
}

module.exports = {checkHash: checkHash, solveTask: solveTask};