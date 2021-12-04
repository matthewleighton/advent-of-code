import numpy as np
import pprint
pp = pprint.PrettyPrinter(indent=4)

def get_numbers_and_cards():
	with open('data.txt') as file:
		numbers = file.readline().strip().split(',')
		remaining_lines = file.readlines()
		cards = []

		for line in remaining_lines:
			if line == '\n':
				cards.append([])
			else:
				card_row = line.strip().replace('  ', ' ').split(' ')
				cards[-1].append(card_row)

		file.close()

	return numbers, cards

def run_next_number():
	target_number = number_list.pop(0)
	update_cards_with_number(target_number)

def update_cards_with_number(target_number):
	global number_of_winners

	for card_id, card in enumerate(card_list):
		for row_id, row in enumerate(card):
			for col_id, number in enumerate(row):
				
				if number == target_number:
					card_list[card_id][row_id][col_id] += ' '

					if check_card_wins(card) and not card_id in winning_ids:
						
						winning_ids.append(card_id)

						if len(winning_ids) == len(card_list):
							calculate_winning_values(card, number)

							return True

def check_card_wins(card):
	if check_rows(card):
		return True

	if check_rows(np.array(card).transpose().tolist()):
		return True

	return False

def check_rows(card):
	for row in card:
		row_wins = True
		for number in row:
			if number[-1] != ' ':
				row_wins = False

		if row_wins:
			return True

def calculate_winning_values(card, winning_number):
	global game_over
	game_over = True

	summation = 0

	for row_id, row in enumerate(card):
		for col_id, number in enumerate(row):
			if number[-1] != ' ':
				summation += int(number)


	winning_score = summation * int(winning_number)

	print(f'Winning Score: {winning_score}')

game_over = False
winning_ids = []
number_list, card_list = get_numbers_and_cards()

while not game_over:
	run_next_number()