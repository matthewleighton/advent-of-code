from math import lcm

def get_data(filename):
    with open(filename) as f:
        lines = [line.rstrip() for line in f.readlines()]
    return {
        "directions": lines[0].replace("L", "0").replace("R", "1"),
        "guide": parse_guide(lines[2:]),
    }

def parse_guide(lines):
    guide = {}
    for line in lines:
        label, sides = line.split(" = ")
        guide[label] = [sides[1:4], sides[6:9]]
    return guide

class Walker:
    def __init__(self, data, start_location="AAA"):
        self.direction_index = 0
        self.directions = data["directions"]
        self.guide = data["guide"]
        self.location = start_location
        self.step_count = 0

    def follow_route(self):
        while self.location != "ZZZ":
            self.take_step()

    def take_step(self):
        direction = int(self.directions[self.direction_index])
        self.location = self.guide[self.location][direction]
        self.step_count += 1
        self.increment_direction_index()

    def increment_direction_index(self):
        self.direction_index += 1
        if self.direction_index >= len(self.directions):
            self.direction_index = 0


def task_1(data):
    walker = Walker(data)
    walker.follow_route()
    return walker.step_count


def task_2(data):
    walkers = []
    for start in data["guide"]:
        if start[2] == "A":
            walkers.append(Walker(data, start_location=start))
    steps_in_loop = [0 for _ in walkers]
    while True:
        for i, walker in enumerate(walkers):
            walker.take_step()
            if (walker.location[2] == "Z"):
                steps_in_loop[i] = walker.step_count
        if 0 not in steps_in_loop:
            break
    return lcm(*steps_in_loop)


data = get_data("data.txt")

task_1_result = task_1(data)
print(f"Task 1: {task_1_result}")

task_2_result = task_2(data)
print(f"Task 2: {task_2_result}")