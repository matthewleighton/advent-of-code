def get_instructions():
	with open('data.txt') as f:
		data = [(line.rstrip() + ' ').split(' ') for line in f.readlines()]

		instructions_list = []

		for line in data:
			instructions_list.append({
				'command': line[0],
				'argument': int(line[1]) if len(line[1]) else None
			})

		f.close()

	return instructions_list


class Cpu():
	TARGET_CYCLES = [20 + x*40 for x in range(6)]
	NUMBER_OF_PIXELS = 240
	SCREEN_WIDTH = 40

	def __init__(self, instructions_list):
		self.instructions_list = instructions_list
		self.register = 1
		self.clock = 1 # This means we are ABOUT TO RUN the first cycle.

		self.initialize_screen()

		self.log = {}
		self.update_log()

	# The screen begins with each pixel empty.
	def initialize_screen(self):
		self.screen = []

		for i in range(self.NUMBER_OF_PIXELS):
			self.screen.append('.')


	def run_program(self):
		for instruction in self.instructions_list:
			self.run_instruction(instruction)


	def run_instruction(self, instruction):
		command  = instruction['command']
		argument = instruction['argument']

		if command == 'addx':
			self.addx(argument)
		elif command == 'noop':
			self.end_cycle()


	def addx(self, argument):
		self.end_cycle()
		self.register += argument
		self.end_cycle()

	# A cycle is complete: update the clock, such that it tells us which cycle will run NEXT.
	def end_cycle(self):
		self.clock += 1
		self.update_log()
		self.update_screen()

	def update_log(self):
		self.log[self.clock] = self.register

	def update_screen(self):
		# The vertical position is controlled by the clock number.
		row_start = (self.clock-1) // self.SCREEN_WIDTH
		
		# The sprite is 3 pixels wide. These are the pixels it currently covers.
		sprite_pixels = [row_start*self.SCREEN_WIDTH + self.register + i for i in [-1, 0, 1]]

		# Pixels are drawn in numerical order. If the sprite covers a pixel being drawn, then fill it.
		if self.clock-1 in sprite_pixels:
			self.screen[self.clock-1] = '#'

	def task_1(self):
		total = 0
		for cycle_number in self.TARGET_CYCLES:
			total += self.log[cycle_number]*cycle_number

		print('Task 1: ', total)


	def render_screen(self):
		number_of_rows = int(self.NUMBER_OF_PIXELS / self.SCREEN_WIDTH)

		row_pixels = [
			self.screen[i*self.SCREEN_WIDTH:(i+1)*self.SCREEN_WIDTH]
			for i in range(number_of_rows)
		]

		for row in row_pixels:
			print(''.join(row))


instructions_list = get_instructions()

cpu = Cpu(instructions_list)
cpu.run_program()
cpu.task_1()
cpu.render_screen()