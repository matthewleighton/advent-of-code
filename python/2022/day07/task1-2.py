def get_data():
	with open('data.txt') as f:
		data = [line.rstrip() for line in f.readlines()]
		f.close()

	return data

class Computer():
	TASK_1_MAX_SIZE = 100000

	def __init__(self, data):
		self.current_position = []
		self.structure = {}

		self.build_computer(data)

	# Build up the computer's file system, based on the task input.
	def build_computer(self, data):
		for line in data:
			self.handle_line(line)

	# Handle one individual line of the task input.
	# Either updating the file strucutre, or moving our position.
	def handle_line(self, line):
		line_type = self.get_line_type(line)

		if line_type == 'command':
			self.execute_command(line)
		else:
			# self.log_output(line)
			self.update_structure(line)

	# Each line of the input file represents either a user command or the output from a command.
	def get_line_type(self, line):
		return 'command' if line[0] == '$' else 'output'		

	# We only actually do any work on cd commands.
	def execute_command(self, line):
		line = line.split(' ')

		command = line[1]
		argument = line[2] if len(line) > 2 else None

		if command == 'cd':
			self.cd(argument)

	# The current position is stored as a list. Update this based on the argument.
	def cd(self, argument):
		if argument == '..':
			self.current_position.pop()
		elif argument == '/':
			self.current_position = []
		else:
			self.current_position.append(argument)

	# First navigate through the file structure to reach the directory containing the file adding.
	# Then add the new file, specifying its size.
	# def update_structure(self, filename, size):
	def update_structure(self, line):
		size, filename = line.split(' ')

		# In the case of directories, their size is not given. Just skip these lines.
		if size == 'dir':
			return

		current_directory = self.get_current_directory()
		current_directory[filename] = size

	# Return sub-dictionary representing the directory pointed at by self.current_position.
	def get_current_directory(self):
		current_directory = self.structure

		for move in self.current_position:
			if move not in current_directory.keys():
				current_directory[move] = {} # Create the directory if it doesn't exist yet.

			current_directory = current_directory[move]

		return current_directory

	# Complete the required tasks.
	def tasks(self):
		self.directory_sizes = []
		self.task_1_solution = 0

		used_size = self.explore_directory(self.structure)
		task_2_solution = self.get_task_2_solution(used_size)

		print('Task 1: ', self.task_1_solution)
		print('Task 2: ', task_2_solution)

	# Recursively explore directories.
	# Returns the directory size (including sub-directories)
	def explore_directory(self, location):
		this_directory_size = 0

		for item_name, value in location.items():
			
			if type(value) is dict: # Handling directories.
				sub_directory_size = self.explore_directory(value)

				self.directory_sizes.append(sub_directory_size)
			
				if sub_directory_size <= self.TASK_1_MAX_SIZE:
					self.task_1_solution += sub_directory_size

				this_directory_size += sub_directory_size
			
			else: # Handling files.
				this_directory_size += int(value)

		return this_directory_size

	# Find the smallest file which can be deleted while freeing enough space.
	def get_task_2_solution(self, used_size):
		computer_size = 70000000
		update_size = 30000000

		remaining_size = computer_size - used_size
		size_needed = update_size - remaining_size
		self.directory_sizes.sort()

		for size in self.directory_sizes:
			if size >= size_needed:
				return size

data = get_data()
computer = Computer(data)
computer.tasks()