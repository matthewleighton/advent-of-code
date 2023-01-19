const helper = require('./helper');

test('handleCharacter returns 1 for (', () => {
	result = helper.handleCharacter('(');
	expect(result).toBe(1);
});

test('handleCharacter returns -1 for )', () => {
	result = helper.handleCharacter(')');
	expect(result).toBe(-1);
});