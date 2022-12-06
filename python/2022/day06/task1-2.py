def get_data():
	with open('data.txt') as f:
		data = f.readline()
		f.close()

	return data

def all_character_unique(string):
	if len(set(string)) == len(string):
		return True

	return False

def task(data, marker_length, task_number):
	i = marker_length

	while True:
		window = data[i-marker_length:i]

		if all_character_unique(window):
			break

		i += 1

	print(f'Task {task_number}: {i}')

data = get_data()

task(data, marker_length=4, task_number=1)
task(data, marker_length=14, task_number=2)