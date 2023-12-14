import math
import re

def get_data(filename) -> list[str]:
	with open(filename) as f:
		raw_data = [re.findall(r'\d+', line) for line in f.readlines()]
	return {
		"times": raw_data[0],
		"distances": raw_data[1]
	}

def get_min_max_time(race_time, record_distance):
	results = [
		(race_time + sign * math.sqrt(race_time**2 - 4*record_distance)) / 2
		for sign in [-1, 1]
	]
	lower = min(results)
	upper = max(results)
	if lower.is_integer():
		lower += 1
	if upper.is_integer():
		upper -= 1
	return math.ceil(lower), math.floor(upper)

def merge_values(values):
	return int("".join([values[i] for i in range(len(values))]))

def task_1(data):
	prod = 1
	for i in range(len(data["times"])):
		race_time = int(data["times"][i])
		record_distance = int(data["distances"][i])
		lower, upper = get_min_max_time(race_time, record_distance)
		prod *= len (range(lower, upper+1))
	return prod

def task_2(data):
	race_time = merge_values(data["times"])
	record_distance = merge_values(data["distances"])
	lower, upper = get_min_max_time(race_time, record_distance)
	return len(range(lower, upper+1))


data = get_data("data.txt")

task_1_result = task_1(data)
task_2_result = task_2(data)

print(f"Task 1: {task_1_result}")
print(f"Task 2: {task_2_result}")