# Silly original method of task 1.

from collections import Counter

def get_data():
	with open('data.txt') as file:
		data = [ line.rstrip() for line in file.readlines()]

		polymer = data[0]
		rule_list = [ rule.split(' -> ') for rule in data[2:] ]

		file.close()
	
	return polymer, rule_list

def get_pairs(polymer):
	pairs = []

	for i in range(len(polymer)-1):
		pairs.append(polymer[i:i+2])

	return pairs

def perform_step(polymer, rule_list):
	pairs = get_pairs(polymer)

	rule_application_list = []

	for i, pair in enumerate(pairs):

		for rule in rule_list:
			if rule[0] == pair:
				rule_application_list.append({
					'i': i+1,
					'character': rule[1]
					})

	rule_application_list.reverse()

	for rule_application in rule_application_list:
		i = rule_application['i']
		character = rule_application['character']

		polymer = polymer[:i] + character + polymer[i:]

	return polymer

def get_score(polymer):
	sorted_characters = Counter(polymer).most_common()

	most_common  = sorted_characters[0][1]
	least_common = sorted_characters[-1][1]

	return most_common - least_common


polymer, rule_list = get_data()

steps_completed = 0

while steps_completed < 10:
	polymer = perform_step(polymer, rule_list)

	steps_completed += 1

score = get_score(polymer)
print(score)