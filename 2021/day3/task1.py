with open('data.txt') as file:
	data = file.readlines()
	data = [line.rstrip() for line in data]

positions = [0] * len(data[0])

for line in data:
	for i, bit in enumerate(line):
		if bit == '1':
			positions[i] += 1
		else:
			positions[i] -= 1

for i, bit in enumerate(positions):
	if int(bit) < 0:
		positions[i] = '0'
	else:
		positions[i] = '1'


gamma = int(''.join(positions), 2)

for i, character in enumerate(positions):
	if character == '1':
		positions[i] = '0'
	else:
		positions[i] = '1'


epsilon = int(''.join(positions), 2)
print(gamma * epsilon)