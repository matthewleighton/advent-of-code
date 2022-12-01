import numpy as np

def get_data():
	with open('data.txt') as file:
		data = file.readlines()
		data = [list( map(int, line.rstrip())) for line in data]

		file.close()
	return np.matrix(data)

def get_adjacent_coords(h, w):
	possible_coords = [
		[h-1, w],
		[h+1, w],
		[h, w-1],
		[h, w+1]
	]

	valid_coords = []

	for c in possible_coords:
		if c[0] < 0 or c[0] >= height:
			continue

		if c[1] < 0 or c[1] >= width:
			continue

		valid_coords.append(c)

	return valid_coords

def is_lowest_point(h, w):
	target_value = data[h, w]
	adjacent_coords = get_adjacent_coords(h, w)

	for c in adjacent_coords:
		if target_value >= data[c[0], c[1]]:
			return False

	return True

def point_already_analysed(h, w):
	if [h, w] in analysed_points:
		return True

	return False

def get_point_value(h, w):
	return data[h, w]

def analyse_basin(h, w):
	if point_already_analysed(h, w):
		return 0

	if get_point_value(h, w) == 9:
		return 0

	analysed_points.append([h, w])
	basin_size = 1

	adjacent_points = get_adjacent_coords(h, w)

	for point in adjacent_points:
		basin_size += analyse_basin(point[0], point[1])

	return basin_size


data = get_data()
height, width = data.shape
h, w = 0, 0

analysed_points = []
basin_sizes = []

for h in range(height):
	for w in range(width):
		
		basin_size = analyse_basin(h, w)

		if basin_size:
			basin_sizes.append(basin_size)
	
basin_sizes.sort(reverse=True)

solution = basin_sizes[0] * basin_sizes[1] * basin_sizes[2]

print(solution)