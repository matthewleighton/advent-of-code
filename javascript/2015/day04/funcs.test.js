const funcs = require('./funcs');

test('checkHash returns False if the first n characters are not zero', () => {
	const key = 'abcdef';
	const inputValue = 12345;
	const n = 5;

	result = funcs.checkHash(key, inputValue, n);

	expect(result).toBeFalsy();
});

test('checkHash returns False if the first n characters are not zero', () => {
	const key = 'abcdef';
	const inputValue = 609043;
	const n = 5;

	result = funcs.checkHash(key, inputValue, n);

	expect(result).toBeTruthy();
});

test('solveTask returns expected results for test data', () => {
	const key = 'abcdef'
	const n = 5;

	result = funcs.solveTask(key, n);

	expect(result).toBe(609043);
});