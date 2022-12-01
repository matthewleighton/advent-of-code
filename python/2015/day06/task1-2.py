import re, numpy as np

def get_data():
	with open('data.txt') as file:
		lines = [line.rstrip() for line in file.readlines()]
		data  = []

		for line in lines:
			data.append({
				'type': get_type(line),
				'start': get_start(line),
				'stop': get_stop(line)
			})

		file.close()
	return data

def get_first_digit_index(line):
	return re.search(r"\d", line).span()[0]-1

def get_type(line):
	return line[:get_first_digit_index(line)]

def get_start(line):
	return list(map(int, line[get_first_digit_index(line)+1:].split(' ')[0].split(',') ))

def get_stop(line):
	index = line.find('through ') + 8

	return list(map(int,line[index:].split(',')))

def count_active_lights(grid):
	return len(np.nonzero(grid)[0])

def do_command(command):
	global grid_1, grid_2

	for x in range(command['start'][0], command['stop'][0]+1):
		for y in range(command['start'][1], command['stop'][1]+1):
			
			command_type = command['type']

			if command_type == 'turn on':
				grid_1[y, x] = 1
				grid_2[y, x] += 1
			elif command_type == 'turn off':
				grid_1[y, x] = 0
				grid_2[y, x] = max(grid_2[y, x]-1, 0)
			elif command_type == 'toggle':
				grid_1[y, x] = int(not grid_1[y, x])
				grid_2[y, x] += 2

data = get_data()
grid_1, grid_2 = np.zeros([1000, 1000]), np.zeros([1000, 1000])

for command in data:
	do_command(command)

task_1_answer = count_active_lights(grid_1)
task_2_answer = int(np.sum(grid_2))

print(f'Task 1: {task_1_answer}\nTask 2: {task_2_answer}')