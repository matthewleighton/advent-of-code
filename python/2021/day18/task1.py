import pprint
pp = pprint.PrettyPrinter(indent=4)

def get_data():
	with open('data.txt') as file:
		data = file.readlines()

		data = [ line.rstrip() for line in data ]

		lines = [] 

		for line in data:
			lines.append(parse_line(line))

		file.close()

	return data

def parse_line(line_string):
	
	print(line_string)

	line_list = []
	position = 0

	for character in line_string:
		if character == '[':
			line_list[position].append([])
			# line_list.insert(position, [])
			# position += 1
		elif character == ']':
			position += 1
		elif character.isdigit():
			line_list[position].append(int(character))
			# line_list.insert(position, int(character))
			position += 1

		print(line_list)


	return line_list

data = get_data()