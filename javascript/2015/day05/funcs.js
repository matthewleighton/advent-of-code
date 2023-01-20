function containsTwoOfPair(string) {
	for (var i = 0; i < string.length-1; i++) {
		var pair = string.slice(i, i+2);
		var left = string.slice(0, i);
		var right = string.slice(i+2, string.length);

		if (left.includes(pair) || right.includes(pair)) {
			return true
		}
	}

	return false;
}
module.exports.containsTwoOfPair = containsTwoOfPair

function containsRepeatWithGap(string) {
	for (var i = 0; i < string.length - 2; i++) {
		if (string[i] == string[i+2]) {
			return true;
		}
	}

	return false;
}
module.exports.containsRepeatWithGap = containsRepeatWithGap;




function checkString(string, taskNumber) {
	if (taskNumber == 1) {
		checks = [containsTwoOfPair, containsRepeatWithGap];
	}

	for (var i = checks.length - 1; i >= 0; i--) {
		if (!checks[i](string)) {
			return false;
		} 
	}

	return true;
}
module.exports.checkString = checkString;


function solveTask1(data) {
	var niceStringCount = 0

	for (var i = data.length - 1; i >= 0; i--) {
		var string = data[i];
		niceStringCount += checkString(string, 1);
	}

	return niceStringCount;
}
module.exports.solveTask1 = solveTask1;