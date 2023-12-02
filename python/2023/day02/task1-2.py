import re

COLORS = ["red", "green", "blue"]
COLOR_LIMITS = {"red": 12, "green": 13, "blue": 14}

def get_data(filename) -> list[str]:
	with open(filename) as f:
		data = [line.rstrip() for line in f.readlines()]
		f.close()
	return data

def parse_game(line: str):
	game_info = []
	for set_info in line.split(":")[1].split(";"):
		game_info.append(parse_set(set_info, game_info))
	return game_info		

def parse_set(set_info, game_info):
	color_counts = {}
	for color in COLORS:
		regex = f"(\d+)(?=\s*{color})"
		result = re.findall(regex, set_info)
		if result:
			color_counts[color] = int(result[0])
		else:
			color_counts[color] = 0

	return color_counts

def game_is_legal(game_info):
	for set_info in game_info:
		for color, amount in set_info.items():
			if amount > COLOR_LIMITS[color]:
				return False
	return True

def get_game_power(game_info):
	color_maxes = {"red": 0, "green": 0, "blue": 0}
	for set_info in game_info:
		for color, amount in set_info.items():
			if amount > color_maxes[color]:
				color_maxes[color] = amount
	return color_maxes["red"] * color_maxes["green"] * color_maxes["blue"]


def tasks(data):
	task_totals = [0, 0]
	for i, line in enumerate(data):
		game_info = parse_game(line)
		if game_is_legal(game_info):
			task_totals[0] += (i+1)
		task_totals[1] += get_game_power(game_info)

	print(f"Task 1: {task_totals[0]}")
	print(f"Task 2: {task_totals[1]}")


data = get_data("data.txt")
tasks(data)