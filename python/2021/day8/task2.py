import collections

# How we define the positions:
#   T
#TL	  TR
#   M	
#BL   BR
#   B

def get_data():
	with open('data.txt') as file:
		lines = file.readlines()
		lines = [line.rstrip().split(' | ') for line in lines]

		data = [{'signal': line[0].split(' '), 'output': line[1].split(' ')} for line in lines]

		file.close()
	return data

# The codes for one, four, seven, and eight all have unique lengths.
def find_one_four_seven_eight_codes(signal):
	for number_code in signal:

		length = len(number_code)

		if length == 2:
			one_code = list(number_code)
		elif length == 3:
			seven_code = list(number_code)	
		elif length == 4:
			four_code = list(number_code)
		elif length == 7:
			eight_code = list(number_code)

	return one_code, four_code, seven_code, eight_code

# A code length of 6 means either a zero, six or nine.
# The top right letter appears in zero and nine, but not in six.
def find_TR_letter(signal, one_code):
	zero_six_or_nine = []

	for number_code in signal:
		length = len(number_code)

		if length == 6:
			zero_six_or_nine += list(number_code)
		
	for character in one_code:
		count = zero_six_or_nine.count(character)

		if count == 2:
			return character

# The bottom right letter is the letter in the one code, which is not the top right letter.
def find_BR_letter(TR_letter, one_code):
	for letter in one_code:
		if letter != TR_letter:
			return letter

# The two, three, and five all have five letters, and are seperated by the top right, and bottom right letters.
def find_two_three_and_five_codes(signal, TR_letter, BR_letter):
	for number_code in signal:
		if len(number_code) != 5:
			continue

		if TR_letter not in number_code:
			five_code = number_code
		elif BR_letter not in number_code:
			two_code = number_code
		else:
			three_code = number_code

	return list(two_code), list(three_code), list(five_code)

# The bottom left letter is in the two code, but not the three code.
def find_BL_letter(signal, two_code, three_code):
	return list(set(two_code).difference(three_code))[0]

# The zero, six, and nine, codes all ahve six characters, and are seperated by the top right and bottom right letters.
def find_zero_six_nine_codes(signal, TR_letter, BL_letter):
	for number_code in signal:
		if len(number_code) != 6:
			continue

		if TR_letter not in number_code:
			six_code = number_code
		elif BL_letter not in number_code:
			nine_code = number_code
		else:
			zero_code = number_code

	return list(zero_code), list(six_code), list(nine_code)

def get_all_number_codes(signal):
	one_code, four_code, seven_code, eight_code = find_one_four_seven_eight_codes(signal)

	TR_letter = find_TR_letter(signal, one_code)
	BR_letter = find_BR_letter(TR_letter, one_code)

	two_code, three_code, five_code = find_two_three_and_five_codes(signal, TR_letter, BR_letter)

	BL_letter = find_BL_letter(signal, two_code, three_code)

	zero_code, six_code, nine_code = find_zero_six_nine_codes(signal, TR_letter, BL_letter)

	return [
		zero_code, one_code, two_code, three_code, four_code,
		five_code, six_code, seven_code, eight_code, nine_code
	]

def decode_value(value, number_codes):
	value = list(value)

	for number, code in enumerate(number_codes):

		if collections.Counter(code) == collections.Counter(value):
			return str(number)

data = get_data()
total = 0

for line in data:
	number_codes = get_all_number_codes(line['signal'])

	signal = line['signal']

	number = ''

	for coded_value in line['output']:
		value = decode_value(coded_value, number_codes)
		number += value

	total += int(number)

print(total)