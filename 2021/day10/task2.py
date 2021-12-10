import math

def get_data():
	with open('data.txt') as file:
		data = file.readlines()
		data = [line.rstrip() for line in data]

		file.close()
	return data

def get_bracket_pair(bracket):
	return closings[openings.index(bracket)]	

data = get_data()

openings = ['[', '(', '<', '{']
closings = [']', ')', '>', '}']

score_values = {
	')': 1,
	']': 2,
	'}': 3,
	'>': 4
}

line_scores = []

for line in data:
	corrupted = False
	required_close = []

	for i, bracket in enumerate(line):

		if bracket in openings:
			required_close.append(get_bracket_pair(bracket))
			
		else:
			if bracket != required_close[-1]:
				corrupted = True
				break
			else:
				required_close.pop()

	if corrupted:
		continue
		
	required_close.reverse()
	score = 0

	for bracket in required_close:
		score *= 5
		score += score_values[bracket]

	line_scores.append(score)

line_scores.sort()
solution = line_scores[math.floor(len(line_scores)/2)]

print(solution)