from tqdm import tqdm

DIRECTIONS = {
    "up": (0, -1),
    "right": (1, 0),
    "down": (0, 1),
    "left": (-1, 0)
}

NEXT_DIRECTION = {
    "up": "right",
    "right": "down",
    "down": "left",
    "left": "up"
}

class LabMap:
    def __init__(self):
        self.map = self.get_data()
        self.direction = "up"
        self.start_position = self.get_start_position()


    def get_data(self):
        with open("data.txt", "r") as f:
            data = [list(line.strip()) for line in f.readlines()]
        self.y_max = len(data) - 1
        self.x_max = len(data[0]) - 1
        return data


    def get_start_position(self):
        for y, row in enumerate(self.map):
            for x, char in enumerate(row):
                if char == "^":
                    return [x, y]
    

    def guard_at_edge(self):
        return self.x == 0 or self.x == self.x_max or self.y == 0 or self.y == self.y_max


    def turn_if_needed(self, new_block_pos=None):
        while True:
            x_direction, y_direction = DIRECTIONS[self.direction]
            next_x, next_y = self.x + x_direction, self.y + y_direction
            if self.map[next_y][next_x] == "#" or new_block_pos and new_block_pos == (next_x, next_y):
                self.direction = NEXT_DIRECTION[self.direction]
            else:
                break


    def mark_visited(self, visited, with_direction=False):
        if with_direction:
            visited.add((self.x, self.y, self.direction))
        else:
            visited.add((self.x, self.y))
        

    def move(self, new_block_pos=None):
        self.turn_if_needed(new_block_pos)
        x_direction, y_direction = DIRECTIONS[self.direction]
        self.x += x_direction
        self.y += y_direction


    def get_visited(self, loop_check=False, block_pos=None):
        self.x, self.y = self.start_position
        self.direction = "up"
        visited = set()
        self.mark_visited(visited, loop_check)

        while not self.guard_at_edge():
            self.move(block_pos)
            if ((self.x, self.y, self.direction)) in visited:
                return True
            self.mark_visited(visited, loop_check)

        if loop_check:
            return False
        return visited

    def task1(self):
        return len(self.get_visited())


    # 1704
    def task2(self):
        positions = self.get_visited()
        loop_triggers = []
        for p in tqdm(positions):
            if list(p) == self.start_position:
                continue
            if self.get_visited(loop_check=True, block_pos=p):
                loop_triggers.append(p)
        return len(loop_triggers)


print("Task 1:", LabMap().task1())
print("Task 2:", LabMap().task2())