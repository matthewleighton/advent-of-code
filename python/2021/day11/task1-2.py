import numpy as np

def get_data():
	with open('data.txt') as file:
		data = file.readlines()
		data = [ list( map(int, line.rstrip() ) ) for line in data ]

		file.close()

	return np.matrix(data)

def increment_all(data):
	data += 1

def get_adjacent_indices(index):
	h, w = index[0], index[1]

	adjacent_indices = [
		(h-1, w-1),
		(h-1, w),
		(h-1, w+1),

		(h, w-1),
		(h, w+1),

		(h+1, w-1),
		(h+1, w),
		(h+1, w+1)
	]

	return adjacent_indices

def check_valid_index(data, index):
	h, w = index[0], index[1]

	if h < 0 or w < 0:
		return False

	max_h, max_w = data.shape

	if h >= max_h or w >= max_w:
		return False

	return True

def increment_adjacent(data, prime_index):
	adjacent_indices = get_adjacent_indices(prime_index)

	for i in adjacent_indices:
		if not check_valid_index(data, i):
			continue

		data[i] += 1


def fire_flashes(data, already_flashed):
	global total_flashes
	finished_flashing = True

	for index, value in np.ndenumerate(data):
		if value > 9 and not already_flashed[index]:
			finished_flashing = False

			increment_adjacent(data, index)
			total_flashes += 1

			already_flashed[index] = 1


	return finished_flashing

def reset_over_9(data):
	for index, value in np.ndenumerate(data):
		if value > 9:
			data[index] = 0

def run_step(data):
	global steps_completed, all_flashed

	already_flashed = np.zeros(data.shape)
	increment_all(data)

	finished_flashing = False

	while not finished_flashing:
		finished_flashing = fire_flashes(data, already_flashed)

	reset_over_9(data)

	if np.all(already_flashed == 1):
		all_flashed = steps_completed+1


data = get_data()
height, width = data.shape

steps_completed = 0
total_flashes = 0
all_flashed = 0

while True:
	run_step(data)

	steps_completed += 1

	if steps_completed == 100:
		print(f'Task 1: {total_flashes}')

	if all_flashed:
		print(f'Task 2: {all_flashed}')
		break