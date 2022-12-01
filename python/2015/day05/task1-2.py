def get_data():
	with open('data.txt') as file:
		data = [line.rstrip() for line in file.readlines()]
		file.close()
	return data

def count_vowels(string):
	vowels = ['a', 'e', 'i', 'o', 'u']
	number_of_vowels = 0

	for character in string:
		if character in vowels:
			number_of_vowels += 1

	return number_of_vowels

def check_if_contains_bad_string(string):
	bad_strings = ['ab', 'cd', 'pq', 'xy']

	for bad in bad_strings:
		if bad in string:
			return True

	return False

def check_if_contains_double_letter(string):
	for i in range(len(string)-1):
		if string[i] == string[i+1]:
			return True

	return False

def contains_repeat_pair(string):
	i = 0
	while i < len(string)-1:
		target_pair = string[i:i+2]

		if string.rindex(target_pair) > i+1:
			return True

		i+=1

	return False

def contains_repeat_with_gap(string):
	for i in range(len(string)-2):
		if string[i] == string[i+2]:
			return True

	return False

def check_task1(string):
	if count_vowels(string) < 3:
		return False

	if check_if_contains_bad_string(string):
		return False

	if not check_if_contains_double_letter(string):
		return False

	return True

def check_task2(string):
	if not contains_repeat_pair(string):
		return False

	if not contains_repeat_with_gap(string):
		return False

	return True

data = get_data()
task1, task2 = [], []

for string in data:
	if check_task1(string):
		task1.append(string)

	if check_task2(string):
		task2.append(string)

print(f'Task 1: {len(task1)}\nTask 2: {len(task2)}')