from pprint import pprint


class LabMap:
    def __init__(self):
        self.map = self.get_data()
        self.visited = []
        self.x_direction = 0
        self.y_direction = -1

    def get_data(self):
        with open("data.txt", "r") as f:
            data = [list(line.strip()) for line in f.readlines()]
        self.y_bounds = [0, len(data)-1]
        self.x_bounds = [0, len(data[0])-1]
        return data

    def get_start_position(self):
        for y, row in enumerate(self.map):
            for x, char in enumerate(row):
                if char == "^":
                    return x, y
    
    def guard_at_edge(self):
        return (
            self.y in self.y_bounds or
            self.x in self.x_bounds
        )

    def turn_guard(self):
        current = [self.x_direction, self.y_direction]
        if current == [0, -1]:
            new = [1, 0]
        elif current == [1, 0]:
            new = [0, 1]
        elif current == [0, 1]:
            new = [-1, 0]
        else:
            new = [0, -1]
        self.x_direction = new[0]
        self.y_direction = new[1]
    
    def check_next_position(self):
        next_x = self.x + self.x_direction
        next_y = self.y + self.y_direction

        if next_x < 0 or next_y < 0:
            return
        if next_x >= len(self.map[0]) or next_y >= len(self.map):
            return
        if self.map[next_y][next_x] == "#":
            self.turn_guard()

    def mark_visited(self):
        self.visited.append(f"{self.x} {self.y}")

    def move(self):
        self.x += self.x_direction
        self.y += self.y_direction
        self.check_next_position()

    def task1(self):
        self.x, self.y = self.get_start_position()
        self.mark_visited()
        while not self.guard_at_edge():
            self.move()
            self.mark_visited()
        return len(set(self.visited))



task1 = LabMap().task1()
print("Task 1:", task1)