const DeliveryTracker = require('./DeliveryTracker')

test('initializes with with house 0:0 visited', () => {
	var tracker = new DeliveryTracker();
	expect(tracker.houses).toEqual({'0:0': 1});
});

test('locationKey created correctly', () => {
	var tracker = new DeliveryTracker();

	const locationKey = tracker.getLocationKey(2, -11);
	expect(locationKey).toBe('2:-11');
});

test('updateHouse adds new house when it does not already exist', () => {
	var tracker = new DeliveryTracker();

	tracker.updateHouse(2, 5);

	expect(tracker.houses['2:5']).toBe(1);
});

test('updateHouse increments existing house count', () => {
	var tracker = new DeliveryTracker();

	tracker.houses = {'5:3': 1};
	tracker.updateHouse(5, 3);	

	expect(tracker.houses).toEqual({'5:3': 2});
});

test('countVisitedHouses counts correctly', () => {
	var tracker = new DeliveryTracker();

	tracker.updateHouse(1, 1);
	tracker.updateHouse(2, 3);
	tracker.updateHouse(2, 3);
	tracker.updateHouse(-1, 5);
	tracker.updateHouse(-1, 5);

	count = tracker.countVisitedHouses();

	expect(count).toBe(4);
});