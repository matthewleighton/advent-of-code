import numpy as np

def get_data():
	with open('data.txt') as f:
		raw_data = [line.rstrip() for line in f.readlines()]
		f.close()

	formatted_data = format_data(raw_data)

	return formatted_data

def format_data(raw_data):
	formatted_data = []

	for line in raw_data:
		split_line = line.split(' ')

		sensor_x = int(split_line[2].split('=')[1].strip(','))
		sensor_y = int(split_line[3].split('=')[1].strip(':'))

		beacon_x = int(split_line[8].split('=')[1].strip(','))
		beacon_y = int(split_line[9].split('=')[1].strip(':'))

		formatted_data.append({
			'sensor': np.array([sensor_x, sensor_y]),
			'beacon': np.array([beacon_x, beacon_y])
		})

	return formatted_data

def count_empty_positions(data):
	empty_position_list = []
	target_row = 2000000

	for entry in data:
		sensor = entry['sensor']
		beacon = entry['beacon']

		sensor_row = sensor[1]
		sensor_column = sensor[0]

		available_distance = get_distance(sensor, beacon)

		distance_to_row = abs(target_row - sensor_row)
		remaining_distance = max(-1, available_distance - distance_to_row)

		left_bound = sensor_column - remaining_distance
		right_bound = sensor_column + remaining_distance + 1

		empty_position_list += list(range(left_bound, right_bound))

	empty_position_list = list(set(empty_position_list))

	remove_beacons_from_empty_position_list(empty_position_list, target_row, data)

	return len(empty_position_list)

def remove_beacons_from_empty_position_list(empty_position_list, target_row, data):
	for entry in data:
		beacon_x, beacon_y = entry['beacon']

		if beacon_y != target_row:
			continue

		if beacon_x in empty_position_list:
			empty_position_list.remove(beacon_x)

def get_distance(sensor, beacon):
	x_distance = abs(sensor[0] - beacon[0])
	y_distance = abs(sensor[1] - beacon[1])

	return x_distance + y_distance


def solve_task_2(data):
	all_neighbour_spaces = get_all_neighbour_spaces(data)
	target_sensor = find_target_sensor(data, all_neighbour_spaces)
	return target_sensor[0]*4000000 + target_sensor[1]

# The target sensor will be in a space which is a neighbour to some beacon, and not included in the region of any beacon.
def find_target_sensor(data, all_neighbour_spaces):
	for sensor_neighbours in all_neighbour_spaces:
		for space in sensor_neighbours:

			space_found = False

			for entry in data:
				sensor = entry['sensor']
				beacon = entry['beacon']

				beacon_distance = get_distance(sensor, beacon)
				space_distance = get_distance(space, sensor)

				if space_distance <= beacon_distance:
					space_found = True
					break

			if not space_found:
				return space

# Get all the spaces which are just outside the bounds of ANY beacon.
def get_all_neighbour_spaces(data):
	all_neighbour_spaces = []

	for entry in data:
		sensor = entry['sensor']
		beacon = entry['beacon']

		sensor_neighbour_spaces = get_sensor_neighbour_spaces(sensor, beacon)
		all_neighbour_spaces.append(sensor_neighbour_spaces)

	return all_neighbour_spaces

# Get all the spaces which are just outside the bounds of any the given beacon.
def get_sensor_neighbour_spaces(sensor, beacon):
	neighbours_list = []
	distance_to_neighbours = get_distance(sensor, beacon) + 1
	x_center, y_center = sensor

	bounds_max = 4000000

	for x in range(x_center - distance_to_neighbours, x_center + distance_to_neighbours + 1):

		if x < 0 or x > bounds_max:
			continue

		spent_distance = abs(x - x_center)
		remaining_distance = distance_to_neighbours - spent_distance

		space = [x, y_center+remaining_distance]

		if 0 <= space[1] <= bounds_max:
			neighbours_list.append(space)

		if remaining_distance != 0:
			space = [x, y_center-remaining_distance]
			if 0 <= space[1] <= bounds_max:
				neighbours_list.append(space)

	return neighbours_list

data = get_data()

task_1 = count_empty_positions(data)
print('Task 1: ', task_1)

task_2 = solve_task_2(data)
print('Task 2: ', task_2)