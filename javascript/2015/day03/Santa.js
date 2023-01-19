class Santa {
	constructor(deliveryTracker) {
		this.x = 0;
		this.y = 0;

		this.tracker = deliveryTracker
	}

	updatePosition(arrow) {
		if (arrow == '^') {
			this.y++;
		} else if (arrow == 'v') {
			this.y--;
		} else if (arrow == '>') {
			this.x++;
		} else if (arrow == '<') {
			this.x--;
		}

		this.tracker.updateHouse(this.x, this.y);
	}
}

module.exports = Santa;