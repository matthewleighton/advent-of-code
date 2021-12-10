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
	']': 57,
	')': 3,
	'>': 25137,
	'}': 1197
}

total_score = 0

for line in data:

	required_close = []

	for i, bracket in enumerate(line):

		if bracket in openings:
			required_close.append(get_bracket_pair(bracket))			
		else:
			if bracket != required_close[-1]:
				total_score += score_values[bracket]
				break
			else:
				required_close.pop()

print(total_score)