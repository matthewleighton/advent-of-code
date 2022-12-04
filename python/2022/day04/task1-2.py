def get_data():
	with open('data.txt') as f:
		data = [line.rstrip() for line in f.readlines()]
		f.close()

	data = format_data(data)

	return data

# Format the data, such that we have a list of elf_pairs,
# each of which contains a list describingthe start/end position.
def format_data(data):
	formatted_data = []

	for line in data:
		elves = line.split(',')

		bounds = [
			list(map(int, bound)) for bound in
			[elf.split('-') for elf in elves]
		]

		formatted_data.append(bounds)

	return formatted_data

# Return True if list_1 is a sublist of list_2.
def is_sublist(list_1, list_2):
	for item in list_1:
		if not list_2.count(item):
			return False

	return True

# Return True if any item from list_1 is also in list_2.
def lists_have_overlap(list_1, list_2):
	for item in list_1:
		if list_2.count(item):
			return True

	return False

def tasks(data):
	task_1_count = 0
	task_2_count = 0

	for elf_pair in data:
		elf_1 = list(range(elf_pair[0][0], elf_pair[0][1]+1))
		elf_2 = list(range(elf_pair[1][0], elf_pair[1][1]+1))

		if is_sublist(elf_1, elf_2) or is_sublist(elf_2, elf_1):
			task_1_count += 1

		if lists_have_overlap(elf_1, elf_2):
			task_2_count += 1

	print('Task 1:', task_1_count)
	print('Task 2:', task_2_count)

data = get_data()
tasks(data)