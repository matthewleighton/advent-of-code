def get_data():
    global GRID_HEIGHT, GRID_WIDTH
    with open("data.txt", "r") as f:
        area_map = [list(line) for line in f.read().split("\n")]
    GRID_HEIGHT = len(area_map)
    GRID_WIDTH = len(area_map[0])
    return parse_locations(area_map)

def parse_locations(data):
    locations = {}
    for y, row in enumerate(data):
        for x, char in enumerate(row):
            if char == ".":
                continue
            if char not in locations:
                locations[char] = []
            locations[char].append((x, y))
    return locations

def position_in_bounds(x, y):
    return 0 <= x < GRID_WIDTH and 0 <= y < GRID_HEIGHT

def traverse_for_antinodes(loc, delta_x, delta_y, direction):
    found_antinodes = []
    x, y = loc[0], loc[1]
    while True:
        x += delta_x * direction
        y += delta_y * direction
        if not position_in_bounds(x, y):
            break
        found_antinodes.append((x, y))
    return found_antinodes

def get_antinodes(locations, task_num=1):
    antinode_positions = set()
    for i, loc_1 in enumerate(locations):
        for loc_2 in locations[0:i] + locations[i+1:-1]:
            delta_x = loc_2[0] - loc_1[0]
            delta_y = loc_2[1] - loc_1[1]
            if task_num == 1:
                found_antinodes = [
                    (loc_2[0] + delta_x, loc_2[1] + delta_y),
                    (loc_1[0] - delta_x, loc_1[1] - delta_y)
                ]
            elif task_num == 2:
                found_antinodes = (
                    traverse_for_antinodes(loc_2, delta_x, delta_y, -1) + 
                    traverse_for_antinodes(loc_1, delta_x, delta_y, 1)
                ) 
            for antinode_pos in found_antinodes:
                if position_in_bounds(antinode_pos[0], antinode_pos[1]):
                    antinode_positions.add(antinode_pos)
    return antinode_positions


def task(data, task_num=1):
    antinodes = {}
    for key, values in data.items():
        antinodes[key] = get_antinodes(values, task_num=task_num)
    union_set = set.union(*antinodes.values())
    # print_map(union_set)
    return len(union_set)


def print_map(antinodes):
    for y in range(GRID_HEIGHT):
        line = ""
        for x in range(GRID_WIDTH):
            if (x, y) in antinodes:
                line += "#"
            else:
                line += "."
        print(line)


data = get_data()

print("Task 1:", task(data, 1))
print("Task 2:", task(data, 2))