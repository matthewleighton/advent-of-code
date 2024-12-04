class WordSearch:
    def __init__(self, task_num):
        self.data = self.get_data()
        self.found_count = 0
        self.word_locations = []
        self.x, self.y = 0, 0
        self.task_num = task_num
        if task_num == 1:
            self.targets = ["XMAS", "SAMX"]
        else:
            self.targets = ["MAS", "SAM"]
        self.target_len = len(self.targets[0])
        


    def get_data(self):
        with open("data.txt", "r") as f:
            return [list(line.strip()) for line in f.readlines()]


    def run(self):
        while self.y < len(self.data):
            self.check_square()

        if self.task_num == 1:
            return self.found_count

        middle_positions = [
            coord[1] for coord in self.word_locations
        ]
        return int(len(
            [coord for coord in middle_positions if middle_positions.count(coord) == 2]
        ) / 2)


    def check_square(self):
        self.movement(x_move=1, y_move=1)
        self.movement(x_move=1, y_move=-1)
        if self.task_num == 1:
            self.movement(x_move=1)
            self.movement(y_move=1)

        if self.x == len(self.data[0])-1:
            self.x = 0
            self.y += 1
        else:
            self.x += 1
    

    def movement(self, x_move=0, y_move=0):
        x, y = self.x, self.y
        letters, coords = [], []
        for _ in range(self.target_len):
            if y < 0 or y >= len(self.data):
                break
            if x >= len(self.data):
                break
            letters.append(self.data[y][x])
            coords.append([y, x])
            x += x_move
            y += y_move
            self.check_letters(letters, coords)


    def check_letters(self, letters, coords):
        if "".join(letters) in self.targets and coords not in self.word_locations:
                self.found_count += 1
                self.word_locations.append(coords)


print("Task 1:", WordSearch(1).run())
print("Task 2:", WordSearch(2).run())