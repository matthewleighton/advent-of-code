with open('data.txt') as file:
	data = file.readlines()
	data = [line.rstrip() for line in data]

x, z, aim = 0, 0, 0

for line in data:
	line = line.split()
	command = line[0]
	value = int(line[1])

	if command == 'down':
		aim += value
	elif command == 'up':
		aim -= value
	elif command == 'forward':
		x += value
		z += aim * value

print(x*z)