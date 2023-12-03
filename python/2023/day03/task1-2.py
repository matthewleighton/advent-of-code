import math

def get_data(filename) -> list[str]:
	with open(filename) as f:
		data = [list(line.rstrip()) for line in f.readlines()]
		f.close()
	return data

class Checker:
	def __init__(self, data):
		self.data = data
		self.max_x = len(data[0]) - 1
		self.max_y = len(data) - 1
		self.reset()
	
	def reset(self):
		self.checked_coords = []
		self.task_numbers = []

	def main_loop(self, func):
		for y, row in enumerate(self.data):
			for x, value in enumerate(row):
				func(y, x, value)

	def task(self, task_number):
		self.reset()
		if task_number == 1:
			self.main_loop(self.task_1_loop)
		else:
			self.main_loop(self.task_2_loop)
		return sum(self.task_numbers)
		
	def task_1_loop(self, y, x, value):
		if not value.isdigit() or not self.is_number_end(y, x):
			return
		number, number_coords = self.build_number(y, x)
		is_symbol_adjacent = self.number_is_symbol_adjacent(number_coords)
		if is_symbol_adjacent:
			self.task_numbers.append(number)
		
	def task_2_loop(self, y, x, value):
		if not value == "*":
			return
		adjacent_numbers = self.get_adjacent_numbers(y, x)
		if len(adjacent_numbers) != 2:
			return
		self.task_numbers.append(math.prod(adjacent_numbers))

	def is_number_end(self, y, x):
		return x == self.max_x or not self.data[y][x+1].isdigit()

	def coords_are_symbol_adjacent(self, y, x):
		is_symbol_adjacent = False
		adjacent_coords = self.get_adjacent_coords(y, x)
		for adj_coord in adjacent_coords:
			adj_character = self.data[adj_coord[0]][adj_coord[1]]
			if self.check_is_symbol(adj_character):
				is_symbol_adjacent = True
		return is_symbol_adjacent
	
	def number_is_symbol_adjacent(self, number_coords):
		is_symbol_adjacent = False
		for coords in number_coords:
			symbol_test = self.coords_are_symbol_adjacent(coords[0], coords[1])
			if symbol_test:
				is_symbol_adjacent = True

		return is_symbol_adjacent

	def check_is_symbol(self, value):
		return not value.isdigit() and value != "."

	def get_adjacent_coords(self, y, x):
		adjacent_coords = []
		for i in range(-1, 2):
			for j in range(-1, 2):
				new_y, new_x = y + i, x + j
				if 0 <= new_y <= self.max_y and 0 <= new_x <= self.max_x:
					adjacent_coords.append([new_y, new_x])
		return adjacent_coords

	def build_number(self, y, x):
		x = self.get_number_start_x(y, x)
		number = ""
		number_coords = []
		while True:
			if self.is_checked_number(y, x):
				break
			number += self.data[y][x]
			self.checked_coords.append([y, x])
			number_coords.append([y, x])
			x += 1
		return int(number), number_coords
	
	def is_checked_number(self, y, x):
		return not (
				x <= self.max_x
				and not [y, x] in self.checked_coords
				and self.data[y][x].isdigit()
			)
	
	def get_number_start_x(self, y, x):
		while x-1 >= 0 and self.data[y][x-1].isdigit():
			x -= 1
		return x

	def get_adjacent_numbers(self, y, x):
		adjacent_numbers = []
		number_start_coords = []
		adjacent_coords = self.get_adjacent_coords(y, x)
		for adj_y, adj_x in adjacent_coords:
			if not self.data[adj_y][adj_x].isdigit():
				continue
			number_start_x = self.get_number_start_x(adj_y, adj_x)
			if [adj_y, number_start_x] in number_start_coords:
				continue
			adjacent_numbers.append(self.build_number(adj_y, number_start_x)[0])
			number_start_coords.append([adj_y, number_start_x])
		return adjacent_numbers
			

checker = Checker(get_data("data.txt"))
task_1_result = checker.task(1)
task_2_result = checker.task(2)
print(f"Task 1: {task_1_result}")
print(f"Task 2: {task_2_result}")
