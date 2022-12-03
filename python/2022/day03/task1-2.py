def get_data():
	with open('data.txt') as f:
		data = [line.rstrip() for line in f.readlines()]
		f.close()

	return data

# Split each line into its first and second half.
def split_lines(data):
	split_data = []

	for line in data:
		halfway = int(len(line)/2)
		first  = line[:halfway]
		second = line[halfway:]

		split_data.append([first, second])

	return split_data

# Return all the letters which exist in both the first and second halves of each line.
def get_duplicates(data):
	all_duplicates = []

	for line in data:
		first, second = line

		line_duplicates = []

		for character in first:
			if second.count(character) and character not in line_duplicates:
				line_duplicates.append(character)

		all_duplicates += line_duplicates

	return all_duplicates

# Get ASCII value, and subtract such that a=1 and A=27.
def get_letter_score(letter):
	subtractor = 38 if letter.isupper() else 96
	return ord(letter) - subtractor

# Convert a list from characters to their corresponding score values.
def get_list_score(character_list):
	values = [get_letter_score(character) for character in character_list]

	return sum(values)

# Three consecutive elves are a group.
def get_elf_groups(data):
	elf_groups = []

	for i, line in enumerate(data):
		if i % 3 == 0:
			elf_groups.append([])

		elf_groups[-1].append(line)

	return elf_groups

# Return a list of the corresponding badge letter for each given elf group.
def get_badge_letters(elf_groups):
	badge_letters = [get_group_badge(group) for group in elf_groups]

	return badge_letters

# The group badge is the letter which exists in all three elves in the group.
def get_group_badge(elf_group):
	first_elf, second_elf, third_elf = elf_group

	for letter in first_elf:
		if second_elf.count(letter) and third_elf.count(letter):
			return letter

def task_1(data):
	data = split_lines(data)
	duplicates = get_duplicates(data)
	final_score = get_list_score(duplicates)

	print('Task 1:', final_score)


def task_2(data):
	elf_groups = get_elf_groups(data)
	badge_letters = get_badge_letters(elf_groups)
	final_score = get_list_score(badge_letters)

	print('Task 2:' ,final_score)


data = get_data()

task_1(data)
task_2(data)