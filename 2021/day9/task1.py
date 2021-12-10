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


data = get_data()
height, width = data.shape
h, w = 0, 0
sum_of_lowest_points = 0

for h in range(height):
	for w in range(width):
		if is_lowest_point(h, w):
			sum_of_lowest_points += (data[h, w] + 1)

print(sum_of_lowest_points)