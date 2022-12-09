def get_instructions_list():
	with open('data.txt') as f:
		data = [line.rstrip().split(' ') for line in f.readlines()]

		instructions_list = [{
			'direction': line[0],
			'amount': int(line[1])
		} for line in data]

		f.close()

	return instructions_list

class Rope():
	def __init__(self, instructions_list, number_of_knots):
		self.instructions_list = instructions_list
		self.knot_position_logs = [[[0,0]] for i in range(number_of_knots)]

	def run_task(self):
		for instruction in self.instructions_list:
			self.run_instruction(instruction)

		return self.count_unique_last_knot_positions()

	def run_instruction(self, instruction):
		direction = instruction['direction']
		amount    = instruction['amount']

		for step_number in range(amount):
			for knot_number in range(len(self.knot_position_logs)):
				x_shift, y_shift = self.get_move_values(knot_number, direction)
				self.move_knot(knot_number, x_shift, y_shift)

	# Get the values for how much in the x and y directions a given knot should move.
	def get_move_values(self, knot_number, direction):
		# The head knot moves according to the direction instruction.
		if knot_number == 0:
			return self.direction_to_values(direction)

		# Knots which are adjacent to their parent do not move.
		if self.check_if_adjacent(knot_number):
			return 0, 0

		# Different rules depending whether the parent knot is in the same line.
		if self.check_if_same_line(knot_number):
			return self.get_line_move(knot_number)
		
		return self.get_diagonal_move(knot_number)

	# Move a particular knot by a given amount.
	def move_knot(self, knot_number, x_shift, y_shift):
		old_x, old_y, _, _ = self.get_this_and_parent_positions(knot_number)

		new_x = old_x + x_shift
		new_y = old_y + y_shift

		self.knot_position_logs[knot_number].append([new_x, new_y])

	# Return the x and y distances that a knot must go, in order to move in-line to its parent.
	def get_line_move(self, knot_number):
		this_x, this_y, parent_x, parent_y = self.get_this_and_parent_positions(knot_number)

		if parent_x > this_x:
			return 1, 0
		elif parent_x < this_x:
			return -1, 0
		elif parent_y > this_y:
			return 0, 1
		elif parent_y < this_y:
			return 0, -1

	# Return the x and y distances that a knot must go, in order to move diagonally to its parent.
	def get_diagonal_move(self, knot_number):
		this_x, this_y, parent_x, parent_y = self.get_this_and_parent_positions(knot_number)

		x_shift = 1 if parent_x > this_x else -1
		y_shift = 1 if parent_y > this_y else -1

		return x_shift, y_shift

	# Return True if this knot is adjacent to its parent.
	def check_if_adjacent(self, knot_number):
		this_x, this_y, parent_x, parent_y = self.get_this_and_parent_positions(knot_number)

		if abs(this_x - parent_x) > 1:
			return False

		if abs(this_y - parent_y) > 1:
			return False

		return True

	# Return True if this knot is in the same line as its parent.
	def check_if_same_line(self, knot_number):
		this_x, this_y, parent_x, parent_y = self.get_this_and_parent_positions(knot_number)

		if this_x == parent_x:
			return True

		if this_y == parent_y:
			return True

		return False

	# Return the x and y positions of this knot and its parent.
	def get_this_and_parent_positions(self, knot_number):
		this_x, this_y = self.knot_position_logs[knot_number][-1]
		parent_x, parent_y = self.knot_position_logs[knot_number-1][-1]

		return this_x, this_y, parent_x, parent_y		

	# Convert an instruction's direction to x and y shift values.
	def direction_to_values(self, direction):
		return {
			'U': [0, 1],
			'D': [0, -1],
			'L': [-1, 0],
			'R': [1, 0]
		}[direction]

	def count_unique_last_knot_positions(self):
		string_list = []
		last_knot_log = self.knot_position_logs[-1]

		for tail_position in last_knot_log:
			tail_string = str(tail_position)

			if tail_position not in string_list:
				string_list.append(tail_position)

		return len(string_list)

instructions_list = get_instructions_list()

task_1_rope = Rope(instructions_list, 2)
task_1_solution = task_1_rope.run_task()

task_2_rope = Rope(instructions_list, 10)
task_2_solution = task_2_rope.run_task()

print('Task 1: ', task_1_solution)
print('Task 2: ', task_2_solution)