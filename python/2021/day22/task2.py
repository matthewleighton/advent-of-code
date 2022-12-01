import pprint
pp = pprint.PrettyPrinter(indent=4)

import numpy as np

def get_data():
	with open('data.txt') as file:
		lines = [line.rstrip() for line in file.readlines()]

		data = []

		for line in lines:
			status = 1 if line.split(' ')[0] == 'on' else 0
			values = [ list(map(int,v[2:].split('..'))) for v in line.split(' ')[1].split(',')]
			
			data.append({
				'status': status,
				'x': [values[0][0], values[0][1]],
				'y': [values[1][0], values[1][1]],
				'z': [values[2][0], values[2][1]]
			})

		file.close()

	return data

def initialize_space(bounds):
	x_size = bounds['x'][0] + bounds['x'][1]
	y_size = bounds['y'][0] + bounds['y'][1]
	z_size = bounds['z'][0] + bounds['z'][1]

	return np.zeros((x_size, y_size, z_size))

def run_instructions(instruction_list, space):
	offset = 50

	for instruction in instruction_list:
		for x in list(range(instruction['x'][0]+offset, instruction['x'][1]+offset+1)):
			for y in list(range(instruction['y'][0]+offset, instruction['y'][1]+offset+1)):
				for z in list(range(instruction['z'][0]+offset, instruction['z'][1]+offset+1)):
					space[x][y][z] = instruction['status']

	return space

def count_active_positions(space):
	max_x, max_y, max_z = space.shape
	total = 0

	for x in range(max_x):
		for y in range(max_y):
			for z in range(max_z):
				total += space[x][y][z]

	return int(total)


def get_bounds(instruction_list):
	min_x = abs(min(instruction_list, key=lambda a:a['x'][0])['x'][0])
	max_x = max(instruction_list, key=lambda a:a['x'][1])['x'][1]

	min_y = abs(min(instruction_list, key=lambda a:a['y'][0])['y'][0])
	max_y = max(instruction_list, key=lambda a:a['y'][1])['y'][1]

	min_z = abs(min(instruction_list, key=lambda a:a['z'][0])['z'][0])
	max_z = max(instruction_list, key=lambda a:a['z'][1])['z'][1]

	return {'x': [min_x, max_x], 'y': [min_y, max_y], 'z': [min_z, max_z]}


data = get_data()

# pp.pprint(data)

bounds = get_bounds(data)

space = initialize_space(bounds)

print(space.shape)

# run_instructions(data, space)
# active_positions = count_active_positions(space)
# print(active_positions)