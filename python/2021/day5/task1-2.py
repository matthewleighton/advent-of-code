import numpy as np

def get_data():
	with open('data.txt') as file:
		data = file.readlines()
		data = [format_data_line(line.rstrip()) for line in data]

		file.close()

	return data

def format_data_line(line):
	points = line.split(' -> ')
	formatted_line = []

	for p in points:
		formatted_line.append([])
		for coord in p.split(','):
			formatted_line[-1].append(int(coord))

	return formatted_line

def get_x1_x2_y1_y1(line):
	return line[0][0], line[1][0], line[0][1], line[1][1]

def update_area_bounds(line):
	global max_x, max_y

	x1, x2, y1, y2 = get_x1_x2_y1_y1(line)

	if x1 > max_x:
		max_x = x1
	
	if x2 > max_x:
		max_x = x2

	if y1 > max_y:
		max_y = y1

	if y2 > max_y:
		max_y = y2

def check_line_follows_axis(line):
	x1, x2, y1, y2 = get_x1_x2_y1_y1(line)
	if x1 != x2 and y1 != y2:
		return False

	return True

def get_clean_world_map(data):
	for line in data:
		update_area_bounds(line)

	return np.zeros([max_y+1, max_x+1])

def update_world_map(vent_points):
	global world_map

	for point in vent_points:
		x, y = point[0], point[1]

		world_map[y, x] += 1

def get_vent_points(line):
	x1, x2, y1, y2 = get_x1_x2_y1_y1(line)

	x_increment = np.sign(x2 - x1)
	y_increment = np.sign(y2 - y1)

	vent_points = [[x1, y1]]

	while x1 != x2 or y1 != y2:

		if x1 != x2:
			x1 += x_increment

		if y1 != y2:
			y1 += y_increment

		vent_points.append([x1, y1])

	return vent_points
		
def count_points_with_multiple_vents():
	multiple_count = 0

	for vents_at_point in np.nditer(world_map):
		if vents_at_point > 1:
			multiple_count += 1

	print(multiple_count)

def main_loop(only_axis_lines=True):
	global max_x, max_y, world_map

	max_x, max_y = 0, 0
	data = get_data()
	world_map = get_clean_world_map(data)

	for line in data:
		if only_axis_lines and not check_line_follows_axis(line):
			continue

		vent_points = get_vent_points(line)

		update_world_map(vent_points)

	count_points_with_multiple_vents()

# Task 1
main_loop()

# Task 2
main_loop(False)