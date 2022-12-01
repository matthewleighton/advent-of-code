with open('data.txt') as file:
	data = file.readlines()
	data = [int(line.rstrip()) for line in data]

increase_count = 0

previous_number = data.pop(0)

for number in data:
	if number > previous_number:
		increase_count += 1
		
	previous_number = number

print(increase_count)