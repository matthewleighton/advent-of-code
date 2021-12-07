import math
import numpy as np

def get_data():
	with open('data.txt') as file:
		data = file.readline().split(',')
		data = [int(number) for number in data]

		file.close()
	
	return data

def get_target(data, task_number=1):
	if task_number == 1:
		return np.median(data)
	else:
		return math.floor(np.mean(data))

def get_fuel(data, target, task_number):
	fuel = 0
	for position in data:
		distance = abs(position - target)

		if task_number == 1:
			fuel += distance
		else:
			fuel += 0.5 * distance * (distance + 1)

	return fuel

data = get_data()

for task_number in [1, 2]:
	target = get_target(data, task_number)
	fuel = get_fuel(data, target, task_number)

	print(f'Task {task_number}: {fuel}')