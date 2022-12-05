import copy

def get_data():
	with open('data.txt') as f:
		data = [line.rstrip() for line in f.readlines()]
		f.close()

	split_point = data.index('')

	raw_stacks = data[:split_point]
	raw_instructions = data[split_point+1:]

	stacks = initialize_stacks(raw_stacks)
	instructions = get_instructions(raw_instructions)

	data = {
		'stacks': stacks,
		'instructions': instructions
	}

	return data

# Format the stacks into their starting positions.
def initialize_stacks(raw_stacks):
	number_of_stacks = int(raw_stacks[-1].split(' ')[-1])
	raw_stacks = raw_stacks[:-1] # Drop last row, which just lists stack numbers.

	formatted_stacks = {i: [] for i in range(1, number_of_stacks+1)}

	for row in raw_stacks:
		i = 0
		while len(row):
			i += 1
			box = row[:3].rstrip()
			row = row[4:] # Remove the space between items.

			if not box: # If there is nothing in this stack position.
				continue

			letter = box[1] # The letter is contained within the box.
			formatted_stacks[i].insert(0, letter)

	return formatted_stacks

# Prepare the instructions to be read.
def get_instructions(raw_instructions):
	formatted_instructions = []

	for row in raw_instructions:
		row = row.split(' ')

		formatted_instructions.insert(0, {
			'amount': int(row[1]),
			'starting_stack': int(row[3]),
			'destination_stack': int(row[5])
		})

	return formatted_instructions

# Complete task 1 or 2.
def task_n(data, task_number):
	# We'll work on a copy of the stacks/instructions, so we don't mess them up for the second task.
	instructions_list = copy.deepcopy(data['instructions'])
	stacks = copy.deepcopy(data['stacks'])
	
	reverse_moving_items = True if task_number == 2 else False

	while len(instructions_list):
		instruction = instructions_list.pop()
		perform_instruction(instruction, stacks, reverse_moving_items)

	solution = get_solution_code(stacks)
	print(f'Task {task_number}:', solution)

# Perform an individual instruction.
def perform_instruction(instruction, stacks, reverse_moving_items=False):
	amount = instruction['amount']
	starting_stack_number = instruction['starting_stack']
	destination_stack_number = instruction['destination_stack']

	moving_items = []

	for i in range(amount):
		moving_items.append(stacks[starting_stack_number].pop())

	if reverse_moving_items:
		moving_items.reverse()

	stacks[destination_stack_number] += moving_items

# The solution code is a string made up from the top items in each stack.
def get_solution_code(stacks):
	code = ''
	for stack in stacks.values():
		code += stack[-1]

	return code

data = get_data()

task_n(data, 1)
task_n(data, 2)