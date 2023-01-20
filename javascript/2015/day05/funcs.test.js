const funcs = require('./funcs');

test('contains3Vowels correctly returns true', () => {
	var string = 'aei';
	var result = funcs.contains3Vowels(string);
	expect(result).toBeTruthy();

	var string = 'xazegov';
	var result = funcs.contains3Vowels(string);
	expect(result).toBeTruthy();

	var string = 'aeiouaeiouaeiou';
	var result = funcs.contains3Vowels(string);
	expect(result).toBeTruthy();
});

test('contains3Vowels correctly returns true', () => {
	var string = 'aefcd';
	var result = funcs.contains3Vowels(string);
	expect(result).toBeFalsy();

	var string = 'abchgf';
	var result = funcs.contains3Vowels(string);
	expect(result).toBeFalsy();

	var string = 'poik';
	var result = funcs.contains3Vowels(string);
	expect(result).toBeFalsy();
});

test('containsDoubleLetter correctly returns true', () => {
	var string = 'xx';
	var result = funcs.containsDoubleLetter(string);
	expect(result).toBeTruthy();

	var string = 'abcdde';
	var result = funcs.containsDoubleLetter(string);
	expect(result).toBeTruthy();

	var string = 'aabbccdd';
	var result = funcs.containsDoubleLetter(string);
	expect(result).toBeTruthy();

	var string = 'abcdefgg';
	var result = funcs.containsDoubleLetter(string);
	expect(result).toBeTruthy();
});

test('containsDoubleLetter correctly returns false', () => {
	var string = 'xax';
	var result = funcs.containsDoubleLetter(string);
	expect(result).toBeFalsy();

	var string = 'abcded';
	var result = funcs.containsDoubleLetter(string);
	expect(result).toBeFalsy();

	var string = 'ababtbcfcdqd';
	var result = funcs.containsDoubleLetter(string);
	expect(result).toBeFalsy();
});


test('doesNotContainBadSegment correctly returns true', () => {
	var string = 'qwerty';
	var result = funcs.doesNotContainBadSegment(string);
	expect(result).toBeTruthy();

	var string = 'agb';
	var result = funcs.doesNotContainBadSegment(string);
	expect(result).toBeTruthy();
});

test('doesNotContainBadSegment correctly returns false', () => {
	var string = 'qweabrty';
	var result = funcs.doesNotContainBadSegment(string);
	expect(result).toBeFalsy();

	var string = 'cdqwerty';
	var result = funcs.doesNotContainBadSegment(string);
	expect(result).toBeFalsy();

	var string = 'qwepqyh';
	var result = funcs.doesNotContainBadSegment(string);
	expect(result).toBeFalsy();

	var string = 'ahxyhj';
	var result = funcs.doesNotContainBadSegment(string);
	expect(result).toBeFalsy();
});



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
	var string = 'ugknbfddgicrmopn';
	var result = funcs.checkString(string, 1);
	expect(result).toBeTruthy();

	var string = 'aaa';
	var result = funcs.checkString(string, 1);
	expect(result).toBeTruthy();
});

test('checkString correctly returns false for task 1', () => {
	var string = 'jchzalrnumimnmhp';
	var result = funcs.checkString(string, 1);
	expect(result).toBeFalsy();

	var string = 'haegwjzuvuyypxyu';
	var result = funcs.checkString(string, 1);
	expect(result).toBeFalsy();

	var string = 'dvszwmarrgswjxmb';
	var result = funcs.checkString(string, 1);
	expect(result).toBeFalsy();
});

test('checkString correctly returns true for task 2', () => {
	var string = 'qjhvhtzxzqqjkmpb';
	var result = funcs.checkString(string, 2);
	expect(result).toBeTruthy();

	var string = 'xxyxx';
	var result = funcs.checkString(string, 2);
	expect(result).toBeTruthy();
});

test('checkString correctly returns false for task 2', () => {
	var string = 'uurcxstgmygtbstg';
	var result = funcs.checkString(string, 2);
	expect(result).toBeFalsy();

	var string = 'ieodomkazucvgmuy';
	var result = funcs.checkString(string, 2);
	expect(result).toBeFalsy();
});