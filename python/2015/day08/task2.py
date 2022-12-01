def get_data():
	with open('data.txt') as f:
		data = [line.rstrip() for line in f.readlines()]
		return data

data = get_data()

original_length = sum( [ len(line) for line in data ] )

new_length = 0

for line in data:
	new_length +=  2 # New outer quote marks
	new_length += len(line) # Original characters
	new_length += line.count('\"') + line.count('\\') # New escape backslashes for quotation marks and backslashes.

print(new_length - original_length)
