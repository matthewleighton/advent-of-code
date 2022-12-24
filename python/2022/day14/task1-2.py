import numpy as np

def get_cave():
	with open('data.txt') as f:
		instruction_list  = [line.rstrip() for line in f.readlines()]
		instruction_list = format_instructions(instruction_list)

	min_x, max_x, min_y, max_y = get_coord_bounds(instruction_list)
	x_offset = min_x

	apply_x_offset(instruction_list, x_offset)

	max_x = max_x - x_offset
	x_spawn_position = 500 - x_offset
	cave = create_cave(instruction_list, max_x, max_y, x_spawn_position)

	return cave, x_spawn_position


# Format the cave shape instructions into a list of lists,
# where the first element represents the x coordinate and the second element is the y coordinate.
def format_instructions(raw_instruction_list):
	formatted_instruction_list = []

	for line in raw_instruction_list:
		coords_list = line.split(' -> ')

		formatted_instruction_list.append([ list(map(int,  coord.split(','))) for coord in coords_list ])

	return formatted_instruction_list

def get_coord_bounds(instruction_list):
	min_y, max_y = 0, 0
	min_x, max_x = 500, 500


	for line in instruction_list:
		for coord in line:
			min_x = min(min_x, coord[0])
			max_x = max(max_x, coord[0])


			max_y = max(max_y, coord[1])

	return min_x, max_x, min_y, max_y

def apply_x_offset(instruction_list, x_offset):
	for line in instruction_list:
		for coord in line:
			coord[0] -= x_offset


def create_cave(instruction_list, max_x, max_y, x_spawn_position):
	cave = np.zeros((max_y+1, max_x+1))

	for line in instruction_list:
		x, y = line[0]

		for coord in line[1:]:
			new_x, new_y = coord

			x_step = np.sign(new_x - x)
			y_step = np.sign(new_y - y)

			cave[y][x] = 1

			while x != new_x or y != new_y:
				x += x_step
				y += y_step

				cave[y][x] = 1

	cave = add_floor(cave)

	return cave

def add_floor(cave):
	row_length = cave.shape[1]
	shape = (1, cave.shape[1])
	empty_row = np.zeros(shape)
	floor_row = np.ones(shape)

	cave = np.vstack([cave, empty_row])
	cave = np.vstack([cave, floor_row])

	return cave


def fill_cave(task_number=1):
	cave_overflowing = False
	sand_count = -1

	while not cave_overflowing:
		cave_overflowing = add_sand(task_number=task_number)
		sand_count += 1

	if task_number == 2:
		sand_count += 1

	print(f'Task {task_number}: ', sand_count)

# Spawn a new sand, and let it move until it stops.
def add_sand(task_number=1):
	global cave
	cave_overflowing = False
	sand_moving = True
	sand_x, sand_y = x_spawn_position, 0

	while sand_moving:
		sand_x, sand_y, sand_moving = move_sand(sand_x, sand_y, task_number)
		skip_move = False

		if task_number == 1:
			if sand_x < 0 or sand_x >= len(cave[0]):
				cave_overflowing = True
				return cave_overflowing

		else:
			if sand_x == x_spawn_position and sand_y == 0:
				return True


	cave[sand_y][sand_x] = 2

	return cave_overflowing

# Find the new position where the sand should move to.
def move_sand(sand_x, sand_y, task_number):
	position_list = [
		[sand_x, sand_y+1],
		[sand_x-1, sand_y+1],
		[sand_x+1, sand_y+1]
	]

	for position in position_list:
		new_x, new_y = position

		new_x = update_cave_size(task_number, new_x)

		blocked = bool(cave[new_y][new_x])

		if not blocked:
			return new_x, new_y, True

	return sand_x, sand_y, False

# Check if the cave grid size needs to be updated in the x direction.
def update_cave_size(task_number, x):
	global cave

	if task_number != 2:
		return x

	if x < 0:
		add_column('left')
		x = 0

	elif x >= len(cave[0]):
		add_column('right')

	return x

# Add a new column to the cave on either the left or the right.
def add_column(side='left'):
	global cave, x_spawn_position

	height = cave.shape[0]

	new_column = np.zeros((height, 1))
	new_column[height-1][0] = 1

	if side == 'left':
		cave = np.hstack((new_column, cave))
		x_spawn_position += 1
	else:
		cave = np.hstack((cave, new_column))


cave, x_spawn_position = get_cave()
fill_cave(task_number=1)

cave, x_spawn_position = get_cave()
fill_cave(task_number=2)