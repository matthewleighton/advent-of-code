def get_data():
	with open('data.txt') as file:
		data = file.readline().rstrip()
		file.close()
	return data

data = get_data()

position = {'x':0, 'y':0}
visited = ['0 0']

for direction in data:
	if direction == '>':
		position['x'] += 1
	elif direction =='<':
		position['x'] -= 1
	elif direction == '^':
		position['y'] += 1
	elif direction == 'v':
		position['y'] -= 1

	visited.append(str(position['x']) + ' ' + str(position['y']))

print(len(set(visited)))