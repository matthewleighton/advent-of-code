import matplotlib.pyplot as plt
import matplotlib.patches as patches

def get_data():
	with open('data.txt') as file:
		data = file.readline().split('=')

		x_bounds = list(map( int, data[1].strip(', y').split('..') ))
		y_bounds = list(map( int, data[2].split('..') ))

		file.close()

	return x_bounds, y_bounds

def update_probe_position(position, velocity):
	position['x'] += velocity['x']
	position['y'] += velocity['y']

	if velocity['x'] > 0:
		velocity['x'] -= 1
	elif velocity['x'] < 0:
		velocity['x'] += 1

	velocity['y'] -= 1

	return position, velocity

def within_target(position):
	if position['x'] < x_bounds[0] or position['x'] > x_bounds[1]:
		return False

	if position['y'] < y_bounds[0] or position['y'] > y_bounds[1]:
		return False

	return True

def fire(velocity):
	position 	     = {'x': 0, 'y': 0}
	trajectory 	     = [position.copy()]
	initial_velocity = velocity.copy()
	attempt_failed   = False
	greatest_height  = 0

	while not attempt_failed:
		position, velocity = update_probe_position(position, velocity)
		trajectory.append(position.copy())

		if position['y'] > greatest_height:
			greatest_height = position['y']

		if within_target(position):
			return greatest_height, trajectory, initial_velocity

		if position['x'] > x_bounds[1]:
			attempt_failed = True
		elif position['y'] < y_bounds[0]:
			attempt_failed = True

	return -1, trajectory, initial_velocity

def prepare_output_data(trajectory):
	x, y = [], []

	for position in trajectory:
		x.append(position['x'])
		y.append(position['y'])

	return x, y

def graph_trajectory(trajectory):
	x, y = prepare_output_data(trajectory)

	target_top_left = (x_bounds[0], y_bounds[0])
	target_width 	= abs(x_bounds[0] - x_bounds[1])
	target_height 	= abs(y_bounds[0] - y_bounds[1])

	print(target_top_left)

	rect = patches.Rectangle(target_top_left, target_width, target_height, linewidth=1, edgecolor='r', facecolor='none')

	fig, ax = plt.subplots()

	ax.add_patch(rect)

	plt.plot(x,y, marker='o')
	plt.show()

x_bounds, y_bounds = get_data()

greatest_height = 0

valid_velocities = []

for x in range(500):
	for y in range(-500, 500):
		velocity = {'x': x, 'y': y}

		height, trajectory, initial_velocity = fire(velocity)

		if height > -1:
			valid_velocities.append(initial_velocity)

		if height > greatest_height:
			greatest_height = height


# velocity = {'x': 6, 'y': 0}
# greatest_height, trajectory, initial_velocity = fire(velocity)
# graph_trajectory(trajectory)

print(f'Task 1: {greatest_height}')
print(f'Task 2: {len(valid_velocities)}')

