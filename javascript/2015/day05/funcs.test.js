const funcs = require('./funcs');

test('containsTwoOfPair correctly returns true', () => {
	var string = 'xyxy';
	var result = funcs.containsTwoOfPair(string);
	expect(result).toBeTruthy();

	var string = 'aabcdefgaa';
	var result = funcs.containsTwoOfPair(string);
	expect(result).toBeTruthy();

	var string = 'abcyyqweyyh';
	var result = funcs.containsTwoOfPair(string);
	expect(result).toBeTruthy();
});

test('containsTwoOfPair correctly returns false', () => {
	var string = 'aaa';
	var result = funcs.containsTwoOfPair(string);
	expect(result).toBeFalsy();

	var string = 'abcyyqweyh';
	var result = funcs.containsTwoOfPair(string);
	expect(result).toBeFalsy();
});

test('containsRepeatWithGap correctly returns true', () => {
	var string = 'xyx';
	var result = funcs.containsRepeatWithGap(string);
	expect(result).toBeTruthy();

	var string = 'abcdefeghi';
	var result = funcs.containsRepeatWithGap(string);
	expect(result).toBeTruthy();

	var string = 'aaa';
	var result = funcs.containsRepeatWithGap(string);
	expect(result).toBeTruthy();
});

test('containsRepeatWithGap correctly returns false', () => {
	var string = 'xyyx';
	var result = funcs.containsRepeatWithGap(string);
	expect(result).toBeFalsy();


	var string = 'abchgc';
	var result = funcs.containsRepeatWithGap(string);
	expect(result).toBeFalsy();
});

test('checkString correctly returns true for task 1', () => {
	var string = 'qjhvhtzxzqqjkmpb';
	var result = funcs.checkString(string, 1);
	expect(result).toBeTruthy();

	var string = 'xxyxx';
	var result = funcs.checkString(string, 1);
	expect(result).toBeTruthy();
});

test('checkString correctly returns false for task 1', () => {
	var string = 'uurcxstgmygtbstg';
	var result = funcs.checkString(string, 1);
	expect(result).toBeFalsy();

	var string = 'ieodomkazucvgmuy';
	var result = funcs.checkString(string, 1);
	expect(result).toBeFalsy();
});