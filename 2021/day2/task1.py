with open('data.txt') as file:
	data = file.readlines()
	data = [line.rstrip() for line in data]

x, z = 0, 0

for line in data:
	line = line.split()
	command = line[0]
	value = int(line[1])

	if command == 'forward':
		x += value
	elif command == 'up':
		z -= value
	elif command == 'down':
		z += value

print(x*z)