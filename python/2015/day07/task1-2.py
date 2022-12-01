def get_data():
	with open('data.txt') as file:
		lines = [line.rstrip() for line in file.readlines()]
		data = {}

		for line in lines:
			input_text, destination = line.split(' -> ')

			operator, operands = parse_input_text(input_text)

			assign_to_data(data, destination, operator, operands)

		file.close()
	return data

def parse_input_text(input_text):
	operator = get_operator(input_text)
	operands = get_operands(input_text, operator)

	return operator, operands

def get_operator(input_text):
	operator_list = ['AND', 'OR', 'NOT', 'RSHIFT', 'LSHIFT']

	for operator in operator_list:
		if operator in input_text:
			return operator
	
	return 'INPUT'

def get_operands(input_text, operator):
	input_text = input_text.replace(operator + ' ', '')
	operands = input_text.split(' ')

	for i, op in enumerate(operands):
		if op.isdigit():
			operands[i] = int(op)

	return operands

def assign_to_data(data, destination, operator, operands):
	data[destination] = {
		'operator': operator,
		'operands': operands
	}

def save_value(wire_name):
	global recorded_values

	wire_value = get_wire_value(wire_name)

	if isinstance(wire_value, int):
		recorded_values[wire_name] = wire_value

	return wire_value

def get_wire_value(wire_name):
	if recorded_values.get(wire_name):
		return recorded_values[wire_name]

	if isinstance(wire_name, int):
		return wire_name

	wire_info = data[wire_name]

	operator = wire_info['operator']
	operands = wire_info['operands']

	value_1 = save_value(operands[0])

	if len(operands) > 1:
		value_2 = save_value(operands[1])	

	if operator == 'INPUT':
		return get_wire_value(value_1)

	if operator == 'AND':
		return perform_and(value_1, value_2)

	if operator == 'OR':
		return perform_or(value_1, value_2)

	if operator == 'NOT':
		return perform_not(value_1)

	if operator == 'RSHIFT':
		return perform_rshift(value_1, value_2)

	if operator == 'LSHIFT':
		return perform_lshift(value_1, value_2)

def perform_not(value_1):
	return value_1 ^ 65535

def perform_or(value_1, value_2):
	return value_1 | value_2

def perform_and(value_1, value_2):
	return value_1 & value_2

def perform_rshift(value_1, value_2):
	return value_1 >> value_2

def perform_lshift(value_1, value_2):
	return value_1 << value_2

data = get_data()
recorded_values = {}

task_1 = get_wire_value('a')

assign_to_data(data, 'b', 'INPUT', [task_1])
recorded_values = {}

task_2 = get_wire_value('a')

print(f'Task 1: {task_1}')
print(f'Task 2: {task_2}')