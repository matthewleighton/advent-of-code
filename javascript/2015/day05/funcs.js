function contains3Vowels(string) {
	const vowels = ['a', 'e', 'i', 'o', 'u'];
	var vowelCount = 0;

	for (var i = string.length - 1; i >= 0; i--) {
		vowelCount += Boolean(vowels.includes(string[i]));

		if (vowelCount >= 3) {
			return true;
		}
	}

	return false;
}
module.exports.contains3Vowels = contains3Vowels;


function containsDoubleLetter(string) {
	for (var i = 0; i < string.length-1; i++) {
		if (string[i] == string[i+1]) {
			return true;
		}
	}

	return false;
}
module.exports.containsDoubleLetter = containsDoubleLetter;


function doesNotContainBadSegment(string) {
	const badSegments = ['ab', 'cd', 'pq', 'xy'];

	for (var i = badSegments.length - 1; i >= 0; i--) {
		if (string.includes(badSegments[i])) {
			return false;
		}
	}

	return true;
}
module.exports.doesNotContainBadSegment = doesNotContainBadSegment;


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
		var checks = [contains3Vowels, containsDoubleLetter, doesNotContainBadSegment];
	} else if (taskNumber == 2) {
		var checks = [containsTwoOfPair, containsRepeatWithGap];
	}

	for (var i = checks.length - 1; i >= 0; i--) {
		if (!checks[i](string)) {
			return false;
		} 
	}

	return true;
}
module.exports.checkString = checkString;


function solveTask(data, taskNumber) {
	var niceStringCount = 0

	for (var i = data.length - 1; i >= 0; i--) {
		var string = data[i];
		niceStringCount += checkString(string, taskNumber);
	}

	return niceStringCount;
}
module.exports.solveTask = solveTask;