const utils = require('../../utils');
const helper = require('./helper');

var data = utils.getData();

totalArea = 0
totalRibbonLength = 0

for (var i = data.length - 1; i >= 0; i--) {
	var [l, w, h] = helper.parseDimensionString(data[i]);

	totalArea += helper.getPackageArea(l, w, h);
	totalRibbonLength += helper.getRibbonLength(l, w, h);

}

console.log('Task 1:', totalArea);
console.log('Task 2:', totalRibbonLength);
