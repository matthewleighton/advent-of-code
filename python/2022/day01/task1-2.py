def get_data():
	with open('data.txt') as f:
		data = [line.rstrip() for line in f.readlines()]
		f.close()

	return data

def solve_problem(data):
	elves = [0]

	for line in data:
		if line == '':
			elves.append(0)
		else:
			elves[-1] += int(line)

	elves.sort()

	task_1 = elves[-1]
	task_2 = sum(elves[-3:])

	print(f'Task 1 {task_1}')
	print(f'Task 2 {task_2}')

data = get_data()
solve_problem(data)
