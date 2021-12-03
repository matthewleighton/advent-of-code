with open('data.txt') as file:
	data = file.readlines()
	data = [int(line.rstrip()) for line in data]

increase_count = 0
previous_value = data[0] + data[1] + data[2]

i = 1
while i < len(data) - 2:
	current_value = data[i] + data[i+1] + data[i+2]

	if current_value > previous_value:
		increase_count += 1

	previous_value = current_value
	i+=1

print(increase_count)