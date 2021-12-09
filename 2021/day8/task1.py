def get_data():
	with open('data.txt') as file:
		lines = file.readlines()
		lines = [line.rstrip().split(' | ') for line in lines]

		data = [{'signal': line[0].split(' '), 'output': line[1].split(' ')} for line in lines]

		file.close()
	return data

data = get_data()
count = 0

for line in data:
	for value in line['output']:
		if len(value) in [2, 3, 4, 7]:
			count += 1

print(count)