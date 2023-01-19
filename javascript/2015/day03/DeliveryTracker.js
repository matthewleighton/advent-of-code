class DeliveryTracker {
	
	constructor() {
		this.houses = {'0:0': 1};
	}

	updateHouse(x, y) {
		const locationKey = this.getLocationKey(x, y);

		if (!this.houses.hasOwnProperty(locationKey)) {
			this.houses[locationKey] = 1;
		} else {
			this.houses[locationKey]++;
		}
	}

	getLocationKey(x, y) {
		return `${x}:${y}`;
	}

	countVisitedHouses() {
		return Object.keys(this.houses).length;
	}
}
module.exports = DeliveryTracker;