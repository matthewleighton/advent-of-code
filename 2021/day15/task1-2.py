import numpy as np
from itertools import product

def get_data():
	with open('data.txt') as file:
		data = np.matrix([ list(line.rstrip()) for line in file.readlines() ], dtype=int)

		file.close()

	return data

def get_task2_data(raw_data):
	task2_data = raw_data

	for axis in range(2):
		incremented_matrix = task2_data

		for i in range(4):
			incremented_matrix = increment_matrix(incremented_matrix)
			task2_data = np.concatenate( (task2_data, incremented_matrix), axis=axis )

	return task2_data

def increment_matrix(matrix):
	new_matrix = matrix.copy()

	new_matrix += 1
	new_matrix[new_matrix > 9] = 1

	return new_matrix

def initialize_progress_dict(data):
	progress_dict = {}

	y, x = 0, 0
	max_y, max_x = data.shape

	combos = list(product(range(max_x), repeat=2))

	for c in combos:
		progress_dict[c] = {'visited': False, 'score': float('inf')}

	progress_dict[(0,0)] = {'visited': True, 'score': 0}

	return progress_dict


def get_remaining_distance(position, target):
	y, x = position
	target_y, target_x = target

	distance = abs(y - target_y) + abs(x - target_x)

	return distance

def get_neighbours(position, data):
	max_y, max_x = data.shape
	y, x = position[0], position[1]

	adjacent_coords = [
		(y-1, x),
		(y+1, x),
		(y, x-1),
		(y, x+1)
	]

	possible_steps = []

	for step in adjacent_coords:
		# print(step[0])
		if step[0] < 0 or step[0] >= max_y:
			continue

		if step[1] < 0 or step[1] >= max_x:
			continue

		possible_steps.append(step)

	return possible_steps

def dijkstra(data):
	progress_dict = initialize_progress_dict(data)

	queue = [(0, 0)]

	while len(queue):
		current_position = queue.pop(0)

		neighbours = get_neighbours(current_position, data)

		for neighbour in neighbours:
			distance = data[neighbour]

			if progress_dict[neighbour]['visited']:
				continue

			old_cost = progress_dict[neighbour]['score']
			new_cost = progress_dict[current_position]['score'] + distance

			if new_cost < old_cost:
				progress_dict[neighbour]['score'] = new_cost
				queue.append(neighbour)

	return progress_dict

task1_data = get_data()
task1_end_position = tuple(np.array(task1_data.shape)-1)
task1_solution = dijkstra(task1_data)
task1_score = task1_solution[task1_end_position]['score']
print(f'Task 1: {task1_score}')

task2_data = get_task2_data(task1_data)
task2_end_position = tuple(np.array(task2_data.shape)-1)
task2_solution = dijkstra(task2_data)
task2_score = task2_solution[task2_end_position]['score']
print(f'Task 2: {task2_score}')