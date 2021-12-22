def get_data():
	with open('data.txt') as file:
		lines = file.readlines()
		
		data = [ line.rstrip().split(' ')[-1] for line in lines ]
		data = list(map(int, data))
		
		file.close()
	
	return data

def is_game_over():
	for score in score_list:
		if score > 999:
			return True
		
	return False
	
def roll_dice():
	global next_roll, times_rolled
	
	total = 0
	
	for i in range(3):
		if next_roll > 100:
			next_roll = 1
		
		total += next_roll
		times_rolled += 1
		next_roll += 1
		
	return total

def get_new_position(move_distance):
	global next_player
	
	original_position = position_list[next_player]
	new_position = (original_position + move_distance) % 10
	
	if new_position == 0:
		new_position = 10
	
	return new_position

def change_player():
	global next_player
	
	if next_player == 0:
		next_player = 1
	else:
		next_player = 0

def take_turn():
	move_distance = roll_dice()
	new_position = get_new_position(move_distance)
	
	position_list[next_player] = new_position
	score_list[next_player] += new_position

times_rolled = 0
next_roll = 1
score_list = [0,0]
next_player = 0

position_list = get_data()

while not is_game_over():
	take_turn()
	change_player()
	
answer = min(score_list) * times_rolled
print(answer)