import numpy as np

def get_data():
	with open('data.txt') as file:

		data = [ 
			list(map(int, line.rstrip().split('x'))) for line in file.readlines()
		]

		file.close()
	return data

def get_gift_paper(gift):
	l, w, h 	  = gift
	sides 		  = [l*w, w*h, h*l]
	smallest_side = min(sides)

	return 2 * sum(sides) + smallest_side

def get_gift_ribbon(gift):
	l, w, h 		   = gift
	smallest_perimeter = 2*min([l+w, w+h, h+l])
	volume 			   = np.prod(gift)

	return smallest_perimeter + volume

data = get_data()
total_paper, total_ribbon = 0, 0

for gift in data:
	total_paper += get_gift_paper(gift)
	total_ribbon += get_gift_ribbon(gift)

print(f'Task 1: {total_paper}')
print(f'Task 2: {total_ribbon}')