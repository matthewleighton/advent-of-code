import numpy as np

def get_data():
	with open('data.txt') as file:
		data = [ line.rstrip() for line in file.readlines() ]

		separator_line = data.index('')

		coords = data[:separator_line]
		fold_instructions = data[separator_line+1:]

		coords = [ [ int(number) for number in line.split(',') ] for line in coords ]

		for i, line in enumerate(fold_instructions):
			instruction_pair = line.split(' ')[2].split('=')

			fold_instructions[i] = {
				'axis': 0 if instruction_pair[0] == 'x' else 1,
				'value': int(instruction_pair[1])
			}

		file.close()

	return coords, fold_instructions

def remove_coord_repeats(coords):
	unique_coords = []

	for c in coords:
		if c in unique_coords:
			continue

		unique_coords.append(c)


	return unique_coords

def perform_fold(coords, instruction_pair):
	axis = instruction_pair['axis']
	instruction_value = instruction_pair['value']

	for i, c in enumerate(coords):
		diff = c[axis] - instruction_value

		if diff < 0:
			continue

		coords[i][axis] = instruction_value - diff

	coords = remove_coord_repeats(coords)

	return coords

def get_max_coords(coords):
	max_x, max_y = 0, 0

	for c in coords:
		if c[0] > max_x:
			max_x = c[0]

		if c[1] > max_y:
			max_y = c[1]

	return max_x, max_y

def get_display_matrix(coords):
	max_x, max_y = get_max_coords(coords)

	matrix = np.full([max_y+1, max_x+1], '░', dtype=str)

	for c in coords:
		matrix[c[1]][c[0]] = '█'

	return matrix

def output_display_matrix(matrix):
	for row in matrix:
		for character in row:
			print(character, end='')
		print('')


coords, fold_instructions = get_data()

for i, instruction in enumerate(fold_instructions):
	coords = perform_fold(coords, instruction)

	if i == 0:
		print(f'Task 1: {len(coords)}')

display_matrix = get_display_matrix(coords)
output_display_matrix(display_matrix)