def get_data():
	with open('data.txt') as f:
		data = [line.rstrip() for line in f.readlines()]
		return data

data = get_data()

total_length = sum( [ len(line) for line in data ] )
character_length = sum( [ len(eval(line)) for line in data ] )

print(total_length - character_length)