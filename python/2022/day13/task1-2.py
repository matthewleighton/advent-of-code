import copy
import numpy as np
from functools import cmp_to_key

def get_raw_data():
	with open('data.txt') as f:
		lines = [line.rstrip() for line in f.readlines()]
		f.close()

	return lines

def format_pairs(raw_data):
	pairs = [[]]

	for line in raw_data:
		if len(line) == 0:
			pairs.append([]) 
		else:
			pairs[-1].append(eval(line))

	return pairs

def get_pairs():
	raw_data = get_raw_data()
	pairs = format_pairs(raw_data)

	return pairs

def is_pair_ordered_correct(pair):
	item_a, item_b = pair

	return compare_items(item_a, item_b)

def force_list(item):
	if type(item) is int:
		item = [item]

	return item

# 1 means list_a comes before list_b
# -1 means the other way around.
# 0 means they are equal,
def compare_lists(list_a, list_b):
	while len(list_a) and len(list_b):
		item_a = list_a.pop(0)
		item_b = list_b.pop(0)

		comparison_result = compare_items(item_a, item_b)

		# Checking if there is a definative result.
		# A value of 0 means equal.
		if comparison_result in [-1, 1]:
			return comparison_result

	if len(list_b) < len(list_a):
		return -1

	if len(list_a) == 0 and len(list_b) > 0:
		return 1

	return 0

def compare_items(item_a, item_b):
	item_a = copy.deepcopy(item_a)
	item_b = copy.deepcopy(item_b)

	if list in [type(item_a), type(item_b)]:
		list_a = force_list(item_a)
		list_b = force_list(item_b)

		return compare_lists(list_a, list_b)

	if item_a < item_b:
		return 1

	if item_a == item_b:
		return 0

	return -1

def get_correct_pair_indices(pairs):
	correct_pair_indices = []

	for i, pair in enumerate(pairs):
		result = is_pair_ordered_correct(pair)

		if result >= 0:
			correct_pair_indices.append(i+1)

	return correct_pair_indices

def solve_task_1(pairs):
	pairs = copy.deepcopy(pairs)
	correct_pair_indices = get_correct_pair_indices(pairs)
	solution = np.sum(correct_pair_indices)

	print('Task 1: ', solution)


def pairs_to_all_lines(pairs):
	all_lines = []

	for line_a, line_b in pairs:
		all_lines.append(line_a)
		all_lines.append(line_b)

	# Adding divider lines.
	all_lines.append([[2]])
	all_lines.append([[6]])

	return all_lines

def get_divider_indices(sorted_lines):
	divider_indices = []
	for i, line in enumerate(sorted_lines):
		if line in [ [[2]], [[6]] ]:
			divider_indices.append(i+1)

	return divider_indices

def solve_task_2(pairs):
	all_lines = pairs_to_all_lines(pairs)
	sorted_lines = sorted(all_lines, key=cmp_to_key(compare_items), reverse=True)
	divider_indices = get_divider_indices(sorted_lines)
	solution = np.prod(divider_indices)

	print('Task 2: ', solution)

pairs = get_pairs()
solve_task_1(pairs)
solve_task_2(pairs)