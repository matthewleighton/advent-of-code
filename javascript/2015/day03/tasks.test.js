funcs = require('./tasks');

test('Task 1', () => {
	var result = funcs.task1('>');
	expect(result).toBe(2);

	var result = funcs.task1('^>v<');
	expect(result).toBe(4);

	var result = funcs.task1('^v^v^v^v^v');
	expect(result).toBe(2);
});

test('Task 2', () => {
	var result = funcs.task2('^v');
	expect(result).toBe(3);

	var result = funcs.task2('^>v<');
	expect(result).toBe(3);

	var result = funcs.task2('^v^v^v^v^v');
	expect(result).toBe(11);
});