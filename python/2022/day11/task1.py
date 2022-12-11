from pprint import pprint

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
		# print('---------perform_turn--------------')
		# print(f'Monkey has {len(self.item_list)} items.')

		for item_id, item in enumerate(self.item_list):
			# print(f'Inspective item {item_id}')
			self.inspect_item(item_id)
			# print(f'Completed item {item_id}.\n')




		self.item_list = []
		# print('TURN COMPLETE!')

	def inspect_item(self, item_id):
		self.perfom_operation(item_id)
		self.divide_worry(item_id)

		destiation_monkey = self.test_true if self.perform_test(item_id) else self.test_false

		monkey_list[destiation_monkey].give_item(self.item_list[item_id])

		self.item_inspection_count += 1


	# For use after item inspection, but before worry level test
	def divide_worry(self, item_id):
		self.item_list[item_id] //= 3

	def perform_test(self, item_id):
		return not bool(self.item_list[item_id] % self.test_value)

	def perfom_operation(self, item_id):
		item = self.item_list[item_id]

		if self.operation_type == '+':
			self.item_list[item_id] += self.operation_argument
			return

		operation_argument = self.item_list[item_id] if self.operation_argument is None else self.operation_argument

		self.item_list[item_id] *= operation_argument




	def give_item(self, item):
		self.item_list.append(item)

	

def perform_round(monkey_list):
	for monkey in monkey_list:
		monkey.perform_turn()


def solve_task_1(monkey_list):
	item_inspection_count_list = [monkey.item_inspection_count for monkey in monkey_list]
	item_inspection_count_list.sort()

	answer = item_inspection_count_list[-1] * item_inspection_count_list[-2]

	print('Task 1: ', answer)

rounds_completed = 0

monkey_list = format_monkeys()

while rounds_completed < 20:
	perform_round(monkey_list)
	rounds_completed += 1
	# print(rounds_completed)


solve_task_1(monkey_list)

