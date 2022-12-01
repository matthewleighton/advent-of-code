def get_data():
	with open('data.txt') as file:
		data = [ line.rstrip() for line in file.readlines()]

		polymer = data[0]
		rule_list = [ rule.split(' -> ') for rule in data[2:] ]

		rule_dict = {}
		for rule in rule_list:
			rule_dict[rule[0]] = rule[1]

		file.close()
	
	return polymer, rule_dict

def get_pairs(polymer):
	pairs = []

	for i in range(len(polymer)-1):
		pairs.append(polymer[i:i+2])

	return pairs

def get_score(character_uses):
	letters = list(character_uses.keys())
	values = list(character_uses.values())

	min_index = values.index(min(values))
	max_index = values.index(max(values))

	score = values[max_index] - values[min_index]

	return score

def get_character_uses(polymer):
	character_uses = {}

	for character in rule_dict.values():
		if character not in character_uses.keys():
			character_uses[character] = 0

	for character in list(polymer):
		character_uses[character] += 1

	return character_uses

def get_pairs_dict():
	pairs_dict = {}

	for pair in rule_dict.keys():
		pairs_dict[pair] = 0

	starting_pairs = get_pairs(polymer)

	for pair in starting_pairs:
		pairs_dict[pair] += 1

	return pairs_dict

# Update pairs_dict and character_uses in accordance to our current setup.
def perform_rule(pair_name, pair_count):
	pairs_dict[pair_name] -= pair_count

	new_character = rule_dict[pair_name]
	character_uses[new_character] += pair_count

	left_side = pair_name[0] + new_character
	right_side = new_character + pair_name[1]

	pairs_dict[left_side] += pair_count
	pairs_dict[right_side] += pair_count

polymer, rule_dict = get_data()

# Keep track of how many times each character appears in our current string.
character_uses = get_character_uses(polymer)

# Keep track of how many of each possible pair exist at the moment.
pairs_dict = get_pairs_dict()

for i in range(40):
	
	# Make a copy, so we don't alter the dictionary as we're working on it.
	for pair_name, pair_count in pairs_dict.copy().items():
		perform_rule(pair_name, pair_count)

score = get_score(character_uses)
print(score)