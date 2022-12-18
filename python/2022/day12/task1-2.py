import numpy as np

def get_data():
	with open('data.txt') as f:
		data = np.array([list(line.rstrip()) for line in f.readlines()])
		f.close()

	return data

def get_coordinates(data, value):
	result = np.where(data == value)

	coords = [
		result[0].item(0),
		result[1].item(0)
	]

	return coords

def get_coords_letter(coords):
	return data[coords[0]][coords[1]]

def initialize_distances():
	distances = {}

	for y, row in enumerate(data):
		distances[y] = {}

		for x, value in enumerate(row):
			distances[y][x] = np.inf


	return distances

def initialize_unexplored_coords():
	unexplored_coords = []

	for y, row in enumerate(data):
		for x, value in enumerate(row):
			coords_string = get_coords_string([y, x])
			unexplored_coords.append(coords_string)

	return unexplored_coords

def get_coords_string(coords):
	y, x = coords
	return str(y) + ':' + str(x)

def check_if_node_explored(coords):
	coords_string = get_coords_string(coords)

	if coords_string in unexplored_coords:
		return False

	return True

def set_distance(coords, value):
	distances[coords[0]][coords[1]] = value

def get_lowest_distance_node_coords():
	lowest_distance = np.inf
	lowest_distance_node_coords = None

	for y, row in enumerate(data):
		for x, value in enumerate(row):
			coords_distance = distances[y][x]

			if coords_distance < lowest_distance and not check_if_node_explored([y, x]):
				lowest_distance = coords_distance
				lowest_distance_node_coords = [y, x]

	return lowest_distance_node_coords

def remove_from_unexplored(coords):
	coords_string = get_coords_string(coords)

	if not coords_string in unexplored_coords:
		return

	index = unexplored_coords.index(coords_string)
	unexplored_coords.pop(index)

def get_adjacent_coords(current_node_coords):
	max_y = len(data)-1
	max_x = len(data[0])-1

	adjacent_coords = []

	for y in [-1, 1]:
		adjacent = [current_node_coords[0]+y, current_node_coords[1]]
		if (0 <= adjacent[0] <= max_y):
			adjacent_coords.append(adjacent)


	for x in [-1, 1]:
		adjacent = [current_node_coords[0], current_node_coords[1]+x]
		if (0 <= adjacent[1] <= max_x):
			adjacent_coords.append(adjacent)

	return adjacent_coords

def is_walkable(current_node_coords, test_node_coords):
	current_node_height = get_node_height(current_node_coords)
	test_node_height = get_node_height(test_node_coords)

	if test_node_height > current_node_height + 1:
		return False

	return True

def get_node_height(node_coords):
	coords_letter = get_coords_letter(node_coords)
	return convert_letter_to_height(coords_letter)


def convert_letter_to_height(letter):
	if letter == 'S':
		letter = 'a'
	elif letter == 'E':
		letter = 'z'

	height = ord(letter) - ord('a')

	return height

def get_potential_new_adjacent_node_distance(current_node_coords, adjacent_coords):
	current_node_distance = get_node_distance(current_node_coords)
	return current_node_distance + 1

def get_node_distance(coords):
	return distances[coords[0]][coords[1]]

def dijkstra():
	while True:
		current_node_coords = get_lowest_distance_node_coords()
		remove_from_unexplored(current_node_coords)
		adjacent_coords_list = get_adjacent_coords(current_node_coords)

		for adjacent_coords in adjacent_coords_list:
			if not is_walkable(current_node_coords, adjacent_coords):
				continue

			if check_if_node_explored(adjacent_coords):
				continue

			potential_new_adjacent_node_distance = get_potential_new_adjacent_node_distance(current_node_coords, adjacent_coords)
			current_adjacent_node_distance = get_node_distance(adjacent_coords)

			if potential_new_adjacent_node_distance < current_adjacent_node_distance:
				set_distance(adjacent_coords, potential_new_adjacent_node_distance)

				if adjacent_coords[0] == end_position[0] and adjacent_coords[1] == end_position[1]:
					return

def initialize_start_positions():
	possible_start_positions = get_possible_start_positions()

	for coords in possible_start_positions:
		set_distance(coords, 0)

def get_possible_start_positions():
	possible_start_positions = []
	for y, row in enumerate(data):
		for x, value in enumerate(row):
			if value in ['S', 'a']:
				possible_start_positions.append([y, x])

	return possible_start_positions

data = get_data()

start_position = get_coordinates(data, 'S')
end_position = get_coordinates(data, 'E')

distances = initialize_distances()
unexplored_coords = initialize_unexplored_coords()

set_distance(start_position, 0)

task_number = 1 if input('Solve which task? ') == '1' else 2

if task_number == 2:
	initialize_start_positions()

dijkstra()

solution = get_node_distance(end_position)
print(f'Task {task_number}: ', solution)