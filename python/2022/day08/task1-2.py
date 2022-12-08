import numpy as np

def get_data():
	with open('data.txt') as f:
		data = [list(map(int, list(line.strip()))) for line in f.readlines()]

		f.close()

	return data

# Return True/False depending whether a given tree is visible from outside the grid.
def is_tree_visible(tree_height, row_number, column_number):
	if is_tree_on_border(row_number, column_number):
		return True

	coords_to_check = get_line_tree_coords(row_number, column_number)

	blocked_sides = []

	for other_coord in coords_to_check:
		blocked_direction = get_blocked_direction(other_coord, row_number, column_number, tree_height)

		if blocked_direction:
			blocked_sides.append(blocked_direction)

	blocked_sides = set(blocked_sides)

	if len(blocked_sides) == 4:
		return False

	return True

def is_tree_on_border(row_number, column_number):
	if 0 in [row_number, column_number]:
		return True

	if row_number == max_row or column_number == max_column:
		return True

	return False

# Return the coordinates for every tree in the same row or column as the target tree.
# (Except for the coordinates of the target tree itself).
def get_line_tree_coords(target_row_number, target_column_number):
	coords = []

	row_number = target_row_number
	for column_number in range(max_column+1):
		if column_number == target_column_number:
			continue
		
		coords.append({'column': column_number, 'row': row_number})

	column_number = target_column_number
	for row_number in range(max_row+1):
		if row_number == target_row_number:
			continue
		
		coords.append({'column': column_number, 'row': row_number})

	return coords

# "Target" refers to the tree we might build the treehouse on. "Other" is the tree potentially blocking it.
# Return False is the tree does not block the target tree.
# If it IS blocked, then return the direction of the other tree relative to the target tree.
def get_blocked_direction(other_coord, target_row, target_column, target_tree_height):
	column = other_coord['column']
	row = other_coord['row']

	other_tree_height = grid[row][column]

	if other_tree_height < target_tree_height:
		return False

	if row > target_row:
		return 'right'

	if row < target_row:
		return 'left'

	if column > target_column:
		return 'bottom'

	return 'top'

# For task 2.
def get_tree_scenic_score(tree_height, row_number, column_number):
	direction_score_dict = {}

	for direction in ['up', 'down', 'left', 'right']:
		direction_score = get_direction_scenic_score(tree_height, row_number, column_number, direction)
		direction_score_dict[direction] = direction_score

	scenic_score = np.prod(list(direction_score_dict.values()))

	return scenic_score

# Get the scenic score for a particular direction (up/down/left/right).
def get_direction_scenic_score(tree_height, row_number, column_number, direction):
	score = 0
	row_increment, column_increment = get_row_and_column_increments(direction)

	while True:
		row_number += row_increment
		column_number += column_increment

		if not (0 <= row_number <= max_row):
			break

		if not (0 <= column_number <= max_column):
			break

		score += 1

		other_tree_height = grid[row_number][column_number]

		if other_tree_height >= tree_height:
			break

	return score

# Get the amounts we need to increment the row/column by to move in a particular direction.
def get_row_and_column_increments(direction):
	return {
		'up':    [-1, 0],
		'down':  [1, 0],
		'left':  [0, -1],
		'right': [0, 1]
	}[direction]


grid = get_data()

max_row = len(grid) - 1
max_column = len(grid[0]) - 1

visible_trees = 0
scenic_score_list = []

for row_number, row in enumerate(grid):
	for column_number, tree_height in enumerate(row):
		
		# Task 1
		if is_tree_visible(tree_height, row_number, column_number):
			visible_trees += 1

		# Task 2
		scenic_score = get_tree_scenic_score(tree_height, row_number, column_number)

		scenic_score_list.append(scenic_score)

best_scenic_score = max(scenic_score_list)

print('Task 1: ', visible_trees)
print('Task 2: ', best_scenic_score)