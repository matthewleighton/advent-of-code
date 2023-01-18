const helper = require('./helper');

test('parseDimensionString reads string correctly', () => {
	var dimensionString = '30x22x25';
	var result = helper.parseDimensionString(dimensionString);

	expect(result).toEqual([30, 22, 25]);
});

test('getPackageArea returns correct area', () => {
	var [l, w, h] = [2, 3, 4]
	var result = helper.getPackageArea(l, w, h);
	expect(result).toBe(58);

	var [l, w, h] = [1, 1, 10]
	var result = helper.getPackageArea(l, w, h);
	expect(result).toBe(43);
});

test('getBowLength returns correct length', () => {
	var [l, w, h] = [2, 3, 4]
	var result = helper.getBowLength(l, w, h);
	expect(result).toBe(24);

	var [l, w, h] = [1, 1, 10]
	var result = helper.getBowLength(l, w, h);
	expect(result).toBe(10);
});

test('getRibbonPerimeterLength returns correct length', () => {
	var [l, w, h] = [2, 3, 4]
	var result = helper.getRibbonPerimeterLength(l, w, h);
	expect(result).toBe(10);

	var [l, w, h] = [1, 1, 10]
	var result = helper.getRibbonPerimeterLength(l, w, h);
	expect(result).toBe(4);
});

test('getRibbonLength returns correct length', () => {
	var [l, w, h] = [2, 3, 4]
	var result = helper.getRibbonLength(l, w, h);
	expect(result).toBe(34);

	var [l, w, h] = [1, 1, 10]
	var result = helper.getRibbonLength(l, w, h);
	expect(result).toBe(14);
});