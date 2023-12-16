def get_data(filename):
	with open(filename) as f:
		return [[[int(x) for x in line.split(" ")]] for line in f.readlines()]

def reduce_reading(reading):
	while any(reading[-1]):
		reading.append([])
		for i in range(len(reading[-2])-1):
			reading[-1].append(reading[-2][i+1] - reading[-2][i])

def extrapolate_reading(reading):
	i = len(reading) - 2
	while i >= 0:
		reading[i].append(reading[i+1][-1] + reading[i][-1])
		reading[i].insert(0, reading[i][0] - reading[i+1][0])
		i -= 1

def tasks(data):
	for reading in data:
		reduce_reading(reading)
		extrapolate_reading(reading)
	task_1_result = sum([data[i][0][-1] for i in range(len(data))])
	task_2_result = sum([data[i][0][0] for i in range(len(data))])
	return task_1_result, task_2_result

data = get_data("data.txt")

task_1_result, task_2_result = tasks(data)
print("Task 1 result: ", task_1_result)
print("Task 2 result: ", task_2_result)