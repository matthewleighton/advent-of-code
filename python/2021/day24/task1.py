import pprint
pp = pprint.PrettyPrinter(indent=4)

def get_data():
	with open('data.txt') as file:
		lines = file.readlines()

		data = [
			line.rstrip().split(' ') for line in lines
		]

		for i, line in enumerate(data):
			if len(line) == 3 and line[2].lstrip('-').isdigit():
				data[i][2] = int(line[2])

		file.close()

	return data

def brute_force_model_numbers(instructions):
	global model_number

	model_number = int('9'*14) + 1
	success = False

	while not success:
		model_number = decrement_model_number(model_number)
		success = check_model_number(instructions)

	return model_number

def decrement_model_number(model_number):
	model_number -= 1

	while True:
		if not '0' in str(model_number):
			break
		model_number -= 1

	# print(model_number)

	return model_number

def check_model_number(instructions):
	global character_position, w, x, y, z, model_number
	w, x, y, z = 0, 0, 0, 0
	character_position = 0

	for line in instructions:
		command = line[0]
		a = line[1]
		if len(line) == 3:
			b = line[2]
		else:
			b = False

		run_instruction(command, a, b)

	if z == 0:
		return True

	return False

def run_instruction(command, a, b=False):
	# if b and not str(b).isdigit():
	if b and not isinstance(b, int):
		b = globals()[b]

	globals()[command](a, b)

def inp(a, b=False):
	global character_position, w, x, y, z, model_number

	globals()[a] = int(str(model_number)[character_position])
	character_position += 1

def add(a, b):
	globals()[a] += b

def sub(a, b):
	globals()[a] -= b

def mul(a, b):
	globals()[a] *= b

def div(a, b):
	globals()[a] = truncate(globals()[a] / b)

def truncate(value):
	return int(str(value).split('.')[0])

def mod(a, b):
	globals()[a] %= b

def eql(a, b):
	globals()[a] = int(globals()[a] == b)

instructions = get_data()
model_number = brute_force_model_numbers(instructions)

print(model_number)