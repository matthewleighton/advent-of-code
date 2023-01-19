const Santa = require('./Santa');
const DeliveryTracker = require('./DeliveryTracker');

function initializeSanta() {
	const tracker = new DeliveryTracker();
	const santa = new Santa(tracker);

	return santa;
}

test('Santa initializes position to 0,0', () => {
	const santa = initializeSanta();

	expect(santa.x).toBe(0);
	expect(santa.y).toBe(0);
});

test('Santa correctly moves up', () => {
	const santa = initializeSanta();

	santa.updatePosition('^');

	expect(santa.x).toBe(0);
	expect(santa.y).toBe(1);
});

test('Santa correctly moves down', () => {
	const santa = initializeSanta();

	santa.updatePosition('v');

	expect(santa.x).toBe(0);
	expect(santa.y).toBe(-1);
});

test('Santa correctly moves left', () => {
	const santa = initializeSanta();

	santa.updatePosition('<');

	expect(santa.x).toBe(-1);
	expect(santa.y).toBe(0);
});

test('Santa correctly moves right', () => {
	const santa = initializeSanta();

	santa.updatePosition('>');

	expect(santa.x).toBe(1);
	expect(santa.y).toBe(0);
});