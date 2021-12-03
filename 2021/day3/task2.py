def find_most_common_in_position(data, position):
	score = 0

	for line in data:
		bit = line[position]
		
		if bit == '0':
			score -= 1
		else:
			score += 1

	if score < 0:
		return '0'
	else:
		return '1'

def remove_lines_not_matching_at_position(data, value, position):
	indices_to_remove = []

	for i, line in enumerate(data):
		bit = line[position]

		if bit != value:
			indices_to_remove.append(i)

	for i in sorted(indices_to_remove, reverse=True):
		del data[i]

def find_key_value(data, find_least_common=True):
	data = data.copy()

	for i in range(len(data)):
		most_common_value = find_most_common_in_position(data, i)

		if find_least_common:
			if most_common_value == '1':
				most_common_value = '0'
			else:
				most_common_value = '1'

		remove_lines_not_matching_at_position(data, most_common_value, i)

		if len(data) == 1:
			break

	return int(''.join(data[0]), 2)


with open('data.txt') as file:
	data = file.readlines()
	data = [line.rstrip() for line in data]

co2 = find_key_value(data, False) # Most common
oxygen = find_key_value(data, True) # Least common

print(co2 * oxygen)