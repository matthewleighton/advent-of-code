# Well approach was silly, after realising how to do part 2 :)

def get_data():
	with open('data.txt') as file:
		data = file.readline().split(',')
		data = [int(number) for number in data]

		file.close()
	return data

data = get_data()
day = 0

while day < 80:
	new_fish_count = 0

	for i, fish in enumerate(data):
		if fish == 0:
			data[i] = 6
			new_fish_count += 1
		else:
			data[i] -= 1

	for fish in range(new_fish_count):
		data.append(8)

	new_fish_count = 0
	day += 1


print(len(data))