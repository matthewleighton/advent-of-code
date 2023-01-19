const utils = require('../../utils');
const DeliveryTracker = require('./DeliveryTracker');
const Santa = require('./Santa');

function task1(data) {
	var tracker = new DeliveryTracker();
	var santa = new Santa(tracker);

	for (var i = data.length - 1; i >= 0; i--) {
		var direction = data[i];
		santa.updatePosition(direction);
	}

	return santa.tracker.countVisitedHouses();
}

function task2(data) {
	var tracker = new DeliveryTracker();
	var realSanta = new Santa(tracker);
	var robotSanta = new Santa(tracker);

	for (var i = 0; i < data.length; i++) {
		var direction = data[i];

		if (i % 2 == 0) {
			realSanta.updatePosition(direction);
		} else {
			robotSanta.updatePosition(direction);
		}
	}

	return realSanta.tracker.countVisitedHouses();
}

module.exports.task1 = task1
module.exports.task2 = task2