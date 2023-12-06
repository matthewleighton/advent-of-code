import math

def get_data(filename) -> list[str]:
	with open(filename) as f:
		data = [line.rstrip() for line in f.readlines()]
	return data

def get_cards(data):
	return [parse_card(card) for card in data]

def parse_card(card):
	halves = card.split("|")
	return {
		"win_nums": [int(i) for i in halves[0].split()[2:]],
		"you_nums": [int(i) for i in halves[1].split()]
	}
	
def get_card_score(card):
	num_matches = get_card_matches(card)
	return math.floor(2**(num_matches-1))

def get_card_matches(card):
	return len(list(set(card["win_nums"]) & set(card["you_nums"])))

def task_1(data):
	total_score = 0
	for card in get_cards(data):
		total_score += get_card_score(card)
	return total_score

def task_2(data):
	cards = get_cards(data)
	card_counts = {i: 1 for i in range(len(cards))}
	for i, card in enumerate(cards):
		for j in range(get_card_matches(card)):
			card_counts[i+j+1] += card_counts[i]
	
	return sum(card_counts.values())

data = get_data("data.txt")
result_1 = task_1(data)
result_2 = task_2(data)

print(f"Task 1: {result_1}")
print(f"Task 2: {result_2}")