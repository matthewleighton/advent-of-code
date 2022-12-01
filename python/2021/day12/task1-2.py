def get_data():
	with open('data.txt') as file:
		data = file.readlines()
		data = [ line.rstrip().split('-') for line in data ]

		file.close()

	return data

def format_data(data):
	cave_dict = {}

	for tunnel in data:
		for cave in tunnel:
			if not cave in cave_dict.keys():
				cave_dict[cave] = []

		cave_dict[tunnel[0]].append(tunnel[1])
		cave_dict[tunnel[1]].append(tunnel[0])

	return cave_dict

# We're only allowed 1 repeat of a small cave, so check if it already exists.
def check_route_contains_small_cave_repeat(cave, route):
	if task_number == 1:
		return True # No repeats allowed in task 1.

	if cave in ['start', 'end']:
		return True

	visited_small_caves = [ cave for cave in route if cave.islower() ]

	if len(visited_small_caves) != len(set(visited_small_caves)):
		return True

	return False

def depth_first_search(graph, cave, route):
	global route_list

	if cave.islower() and cave in route and check_route_contains_small_cave_repeat(cave, route):
		return

	route.append(cave)

	for neighbour in graph[cave]:

		this_route = route.copy()

		if cave == 'end':
			route_list.append(route)
			return

		depth_first_search(graph, neighbour, this_route)


data = get_data()
cave_dict = format_data(data)

task_number = 1
route_list = []
depth_first_search(cave_dict, 'start', [])
print(f'Task 1: {len(route_list)}')

task_number = 2
route_list = []
depth_first_search(cave_dict, 'start', [])
print(f'Task 2: {len(route_list)}')