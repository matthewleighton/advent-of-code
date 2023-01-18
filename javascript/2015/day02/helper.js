function parseDimensionString(dimensionString) {
	return dimensionString.split('x').map(Number);
}
module.exports.parseDimensionString = parseDimensionString

function getPackageArea(l, w, h) {
	const partOne = 2*l*w + 2*w*h + 2*h*l;
	const partTwo = Math.min(l*w, l*h, w*h);

	const packageArea = partOne + partTwo;

	return packageArea;
}
module.exports.getPackageArea = getPackageArea

function getBowLength(l, w, h) {
	return l*w*h;
}
module.exports.getBowLength = getBowLength;

function getRibbonPerimeterLength(l, w, h) {
	return Math.min(2*(l+w), 2*(l+h), 2*(w+h));
}
module.exports.getRibbonPerimeterLength = getRibbonPerimeterLength;

function getRibbonLength(l, w, h) {
	return getBowLength(l, w, h) + getRibbonPerimeterLength(l, w, h);
}
module.exports.getRibbonLength = getRibbonLength;