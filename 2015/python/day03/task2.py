def get_data():
	with open('data.txt') as file:
		data = file.readline().rstrip()
		file.close()
	return data

data = get_data()

position = [
	{'x':0, 'y':0},
	{'x':0, 'y':0}
]
visited = ['0 0']

for i, direction in enumerate(data):
	pos = position[i % 2]

	if direction == '>':
		pos['x'] += 1
	elif direction =='<':
		pos['x'] -= 1
	elif direction == '^':
		pos['y'] += 1
	elif direction == 'v':
		pos['y'] -= 1

	visited.append(str(pos['x']) + ' ' + str(pos['y']))

print(len(set(visited)))