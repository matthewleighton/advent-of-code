import numpy as np

def get_data():
	with open('data.txt') as f:
		lines = [line.rstrip() for line in f.readlines()]
		data = [line.split(' ') for line in lines]
		f.close()

	return data

def format_turn_data(turn_data):
	return letter_to_number(turn_data[0]), letter_to_number(turn_data[1])

# 1=rock, 2=paper, 3=scissors
def letter_to_number(letter):
	letter_list = ['A', 'X', 'B', 'Y', 'C', 'Z']
	return int(np.ceil((letter_list.index(letter)+1)/2))

# 3>2 | 2>1 | 1>3
def get_user_win_score(p1, p2):
	if p1 == p2:
		return 3 # Draw

	p1 = add_to_shape(p1, -1)

	if p1 == p2:
		return 6 # Win

	return 0 # Lose

# Add a value to the shape, with the logic that 0 cycles up to 3, while 4 cycles down to 1.
def add_to_shape(shape, value):
	shape += value

	if shape == 0:
		shape = 3
	elif shape == 4:
		shape = 1

	return shape

def get_turn_score(p1, p2):
	user_win_score = get_user_win_score(p1, p2)
	user_shape_score = p1

	turn_score = user_win_score + user_shape_score

	return turn_score

def task_1(data):
	user_score = 0

	for turn in data:
		p2, p1 = format_turn_data(turn)
		user_score += get_turn_score(p1, p2)

	print('task_1', user_score)

def task_2(data):
	user_score = 0

	for turn in data:
		opponent_shape, instruction = format_turn_data(turn)

		win_score = {1:0, 2:3, 3:6}[instruction]

		if instruction == 1:
			shape = add_to_shape(opponent_shape, -1) # Lose
		elif instruction == 2:
			shape = opponent_shape # Draw
		elif instruction == 3:
			shape = add_to_shape(opponent_shape, 1) # Win

		user_score += shape + win_score
		
	print('task_2', user_score)

data = get_data()

task_1(data)
task_2(data)