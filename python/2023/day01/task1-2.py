WORDS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def get_data() -> list[str]:
	with open('data.txt') as f:
		data = [line.rstrip() for line in f.readlines()]
		f.close()

	return data


def get_digits(string: str) -> list[str]:
	return [c for c in string if c.isdigit()]


def combine_digits(digits: list[str]) -> int:
	return int(digits[0] + digits[-1])


def replace_words(line: str):
	done = False
	while not done:
		line, done = replace_first_word(line)
	return line


def replace_first_word(line: str):
	first_word = None
	first_index = 9999
	for word in WORDS:
		if word in line and line.index(word) < first_index:
			first_word = word
			first_index = line.index(word)

	if not first_word:
		return line, True
	
	digit = str(WORDS.index(first_word) + 1) + first_word[-1]	
	return line.replace(first_word, digit), False
	

def convert_words(words: list[str]) -> list[str]:
	return [WORDS.index(str(w)) + 1 for w in words]
	

def task(data, task_num) -> int:
	sum = 0
	for line in data:
		if task_num == 2:
			line = replace_words(line)
		digits = get_digits(line)
		sum += combine_digits(digits)
	return sum


data = get_data()
task_1_result = task(data, 1)
task_2_result = task(data, 2)

print(f"Task 1: {task_1_result}")
print(f"Task 2: {task_2_result}")
