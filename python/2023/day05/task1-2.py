def get_data(filename) -> list[str]:
	with open(filename) as f:
		data = [line.rstrip() for line in f.readlines()]
	return data

def parse_data(data):
	return get_seeds(data), group_data(data)

def get_seeds(data):
	return [int(i) for i in data[0].split(" ")[1:]]

def group_data(data):
	grouped_data = []
	for line in data[1:]:
		if line == "":
			if len(grouped_data):
				grouped_data[-1] = sorted(grouped_data[-1], key=lambda x: x[1])
			grouped_data.append([])
			continue
		if "-" in line:
			continue
		grouped_data[-1].append([int(i) for i in line.split(" ")])
	return grouped_data

def find_location(index, routes):
	for stage_number in range(len(routes)):
		for band in routes[stage_number]:
			if band[1] <= index < band[1] + band[2]:
				index += (band[0] - band[1])
				break
	return index

def segment_seeds(seeds):
	seeds = [[seeds[2*i], seeds[2*i] + seeds[(2*i)+1]-1] for i in range(int(len(seeds)/2))]
	return sorted(seeds, key=lambda x: x[0])

def task_1(data):
	seeds, routes = parse_data(data)
	return min([find_location(seed, routes) for seed in seeds])

def task_2(data):
	seeds, guide = parse_data(data)
	segments = [segment_seeds(seeds)]
	for stage in guide:
		segments.append([])
		for seed_segment in segments[-2]:
			seed_start = seed_segment[0]
			seed_end = seed_segment[1]
			for band in stage:
				destination_start = band[0]
				origin_start = band[1]
				origin_end = origin_start + band[2] - 1
				delta = destination_start - origin_start
				# TODO: Finish part 2.
				# Keep track of the start/end of each "region"/"bucket"
				# as we move through the transformations.
				# We don't need to know every digit's value - there's too many of them.
				# Knowing the edge values is enough.
				


data = get_data("data.txt")
task_1_result = task_1(data)
print("Task 1: ", task_1_result)

# task_2_result = task_2(data)
# print("Task 2: ", task_2_result)