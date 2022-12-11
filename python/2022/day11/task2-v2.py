import numpy as np

def format_monkeys():
	with open('data.txt') as f:
		data = [line.rstrip() for line in f.readlines()]
		f.close()

	monkey_list = []

	while len(data):
		monkey_list.append(create_next_monkey(data))

	return monkey_list

def create_next_monkey(data):
	test = data.pop(0) # First line not needed.
	starting_items = [int(item.strip(',')) for item in data.pop(0).split(' ')[4:]]

	operation_line = data.pop(0)
	operation_type = '*' if '*' in operation_line else '+'
	operation_argument = operation_line.split(operation_type)[1].strip()

	if operation_argument.isnumeric():
		operation_argument = int(operation_argument)
	else:
		operation_argument = None

	test_value = int(data.pop(0).split(' ')[-1])
	test_true  = int(data.pop(0).split(' ')[-1])
	test_false = int(data.pop(0).split(' ')[-1])

	if len(data):
		data.pop(0) # Remove the empty line between monkeys.

	return Monkey(starting_items, operation_type, operation_argument, test_value, test_true, test_false)

class Monkey():
	def __init__(self, starting_items, operation_type, operation_argument, test_value, test_true, test_false):
		self.item_list = starting_items
		self.operation_type = operation_type
		self.operation_argument = operation_argument
		self.test_value = test_value
		self.test_true = test_true
		self.test_false = test_false

		self.item_inspection_count = 0


	def __repr__(self):
		items_string = ', '.join(self.item_list)

		value = f'Items: {items_string}\n'
		value += f'Operation Type: {self.operation_type}\n'
		value += f'Operation Argument: {self.operation_argument}\n'
		value += f'Test Value: {self.test_value}\n'
		value += f'Test True: {self.test_true}\n'
		value += f'Test False: {self.test_false}\n'

		return value

	def perform_turn(self):
		for item_id, item in enumerate(self.item_list):
			self.inspect_item(item_id)

		self.item_list = []

	def inspect_item(self, item_id):
		self.perfom_operation(item_id)

		if task_number == 1:
			self.divide_worry(item_id)

		destiation_monkey = self.test_true if self.perform_test(item_id) else self.test_false

		monkey_list[destiation_monkey].give_item(self.item_list[item_id])

		self.item_inspection_count += 1


	# For use after item inspection, but before worry level test
	def divide_worry(self, item_id):
		self.item_list[item_id] //= 3

	# Do the test to check which moneky an item should be given to.
	def perform_test(self, item_id):
		return not bool(self.item_list[item_id] % self.test_value)

	def perfom_operation(self, item_id):
		item = self.item_list[item_id]

		if self.operation_type == '+':
			self.item_list[item_id] += self.operation_argument
		else:
			operation_argument = self.item_list[item_id] if self.operation_argument is None else self.operation_argument
			self.item_list[item_id] *= operation_argument

		if task_number == 2:
			self.floor_worry_value(item_id)

	# For task 2, the effect of the division tests essentially resets each time we pass the lowest common multiple of
	# the test values. Therefore, to keep the numbers low, we increase the numbers in a circle:
	# Each time they reach the LCM value, they become zero again.
	def floor_worry_value(self, item_id):
		self.item_list[item_id] = self.item_list[item_id] % lowest_common_multiple

	# Give an item to a different monkey.
	def give_item(self, item):
		self.item_list.append(item)

	

def perform_round(monkey_list):
	for monkey in monkey_list:
		monkey.perform_turn()

def get_lowest_common_multiple(monkey_list):
	test_values = [monkey.test_value for monkey in monkey_list]

	return np.prod(test_values)


def solve_task(monkey_list):
	item_inspection_count_list = [monkey.item_inspection_count for monkey in monkey_list]
	item_inspection_count_list.sort()

	answer = item_inspection_count_list[-1] * item_inspection_count_list[-2]

	print(f'Task {task_number}: ', answer)


max_round_values = {
	1: 20,
	2: 10000
}

for task_number in [1, 2]:
	rounds_completed = 0
	monkey_list = format_monkeys()
	lowest_common_multiple = get_lowest_common_multiple(monkey_list)


	while rounds_completed < max_round_values[task_number]:
		perform_round(monkey_list)
		rounds_completed += 1


	solve_task(monkey_list)