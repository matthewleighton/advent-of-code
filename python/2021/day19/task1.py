import numpy as np
import itertools

import pprint
pp = pprint.PrettyPrinter(indent=4)

def get_data():
	with open('data.txt') as file:

		lines = [ line.rstrip() for line in file.readlines() ]

		data = []
		for line in lines:
			if line == '':
				continue

			if 'scanner' in line:
				data.append([])
			else:
				data[-1].append(
					np.matrix(list(map( int, line.split(',') ))).transpose()
				)

		file.close()

	return data

def find_overlaps(first_scanner, second_scanner):
	first_scanner, second_scanner = first_scanner.copy(), second_scanner.copy()

def rotate_position(position, rotation):
	rotated_position = rotation.dot(position)
	return rotated_position


def rotate_beacons(beacon_list, rotation_matrix):

	for i, beacon in enumerate(beacon_list):
		beacon_list[i] = rotation_matrix.dot(beacon)

	return beacon_list

def test_overlaps(first_scanner, second_scanner):
	for prime_beacon in first_scanner:
		
		# All the becons detected by the second scanner, normalized such that one of them is at the origin.
		normalized_first_scanner = normalize_to_beacon(first_scanner, prime_beacon)

		for sub_beacon in second_scanner:
			normalized_second_scanner = normalize_to_beacon(second_scanner, sub_beacon)

			# pp.pprint(normalized_first_scanner)
			# pp.pprint(normalized_first_scanner)
			# print('\n\n')

			number_of_overlaps = count_overlaps(normalized_first_scanner, normalized_second_scanner)



def normalize_to_beacon(beacon_list, target_beacon):
	offset = -target_beacon

	normalized_beacon_list = []

	for beacon in beacon_list:
		normalized_beacon_list.append( beacon + offset)

	return normalized_beacon_list


def count_overlaps(first_scanner, second_scanner):
	number_of_overlaps = 0

	for beacon in second_scanner:
		if is_matrix_in_list(beacon, first_scanner):
			number_of_overlaps += 1

def is_matrix_in_list(the_matrix, the_list):
	for test_matrix in the_list:
		if np.array_equal(test_matrix, the_matrix):
			return True

	return False




beacon_positions = get_data()

# pp.pprint(beacon_positions)

R_x = np.matrix([
	[1, 0, 0],
	[0, 0, -1],
	[0, 1, 0]
])

R_y = np.matrix([
	[0, 0, 1],
	[0, 1, 0],
	[-1, 0, 0]
])

R_z = np.matrix([
	[0, -1, 0],
	[1, 0, 0],
	[0, 0, 1]
])


for combo in itertools.combinations(range(len(beacon_positions)), 2):
	print(combo)

	first_scanner, second_scanner = beacon_positions[combo[0]].copy(), beacon_positions[combo[1]].copy()

	# pp.pprint(second_scanner)

	for i in range(4):
		second_scanner = rotate_beacons(second_scanner, R_x)

		for i in range(4):
			second_scanner = rotate_beacons(second_scanner, R_y)

			overlaps_found = test_overlaps(first_scanner, second_scanner)

	# pp.pprint(second_scanner)
