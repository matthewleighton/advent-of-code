def get_data():
	with open('data.txt') as file:
		data = file.readline().rstrip()

		file.close()
	return data

data = get_data()

floor = 0
entered_basement = False

for i, character in enumerate(data):
	if character == '(':
		floor += 1
	elif character == ')':
		floor -= 1

		if not entered_basement and floor < 0:
			entered_basement = i+1

print(f'Task 1: {floor}')
print(f'Task 2: {entered_basement}')