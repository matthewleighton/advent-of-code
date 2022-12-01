import numpy as np

def get_day_list():
	day_list = [0] * 9
	with open('data.txt') as file:
		data = file.readline().split(',')
		for d in data:
			day_list[int(d)] += 1

		file.close()

	return day_list

day_list = get_day_list()
current_day = 0

while current_day < 256:
	new_fishies = day_list[0]

	for i in range(len(day_list)-1):
		day_list[i] = day_list[i+1]

	day_list[6] += new_fishies
	day_list[8] = new_fishies

	current_day += 1

print(np.sum(day_list))