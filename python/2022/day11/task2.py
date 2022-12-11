from pprint import pprint

from time import perf_counter

import math
from functools import reduce

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
	starting_item_values = [int(item.strip(',')) for item in data.pop(0).split(' ')[4:]]

	starting_items = []

	for item_values in starting_item_values:
		starting_items.append(Item(item))

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

class Item():
	def __init__(self, initial_worry):
		self.prime_factors = self.initialize_prime_factors(initial_worry)
		self.addition_value = 0

	def initialize_prime_factors(self, initial_worry):
		return self.get_primes_dict(initial_worry)

	def get_primes_dict(self, n):
		# First we get a list of all the prime factors.
		# Taken from here: https://stackoverflow.com/a/16007256/4897798
		factor_list = []
		while n > 1:
			for i in range(2, n + 1):
				if n % i == 0:
					n //= i
					factor_list.append(i)
					break

		# Then we convert that into a dict.
		# Keys are the primes, values are how many times the prime is used.
		primes_dict = {}
		for f in factor_list:
			if f not in primes_dict.keys():
				primes_dict[f] = 0

			primes_dict[f] += 1

		return primes_dict

	def add(self, value):
		self.addition_value += value

	def multiply(self, value):
		multiplication_factors = self.get_primes_dict(value)

		for prime, amount in multiplication_factors.items():
			if prime not in self.prime_factors.keys():
				self.prime_factors[prime] = 0

			self.prime_factors[prime] += amount



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
			# self.item_list[item_id] += self.operation_argument
			# return
			self.item_list[item_id].add(self.operation_argument)
			return

		operation_argument = self.item_list[item_id] if self.operation_argument is None else self.operation_argument

		# self.item_list[item_id] *= operation_argument
		self.item_list[item_id].multiply(self.operation_argument)




	def give_item(self, item):
		self.item_list.append(item)

	

def perform_round(monkey_list):

	start = perf_counter()

	for monkey in monkey_list:
		monkey.perform_turn()

	end = perf_counter()

	# print(end-start)


def solve_task_1(monkey_list):
	item_inspection_count_list = [monkey.item_inspection_count for monkey in monkey_list]
	item_inspection_count_list.sort()

	answer = item_inspection_count_list[-1] * item_inspection_count_list[-2]

	print('Task 1: ', answer)

rounds_completed = 0

monkey_list = format_monkeys()

# while rounds_completed < 10000:
# 	perform_round(monkey_list)
# 	rounds_completed += 1
# 	print(rounds_completed)


# solve_task_1(monkey_list)

