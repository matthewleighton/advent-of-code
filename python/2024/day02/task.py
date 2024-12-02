def get_data():
    with open("data.txt", "r") as f:
        return [
            [
                int(x) for x in line.rstrip().split(" ")
            ]
            for line in f.readlines()
        ]

def get_sign(x):
    return 1 if x > 0 else -1 if x < 0 else 0

def task1(data):
    valid_lines = []
    for line in data:
        if is_line_valid(line):
            valid_lines.append(line)
    return len(valid_lines)


def task2(data):
    valid_lines = []
    for line in data:
        if check_line_versions(line):
            valid_lines.append(line)
    return len(valid_lines)

def check_line_versions(line):
    removal_index = -1
    while removal_index < len(line):
        if removal_index == -1:
            test_line = line
        else:
            test_line = [x for i, x in enumerate(line) if i != removal_index]
        if is_line_valid(test_line):
            return True
        removal_index += 1
    return False

def is_line_valid(line):
    direction = get_sign(line[1] - line[0])
    for i in range(len(line) - 1):
        change = line[i+1] - line[i]
        if not 1 <= abs(change) <= 3:
            return False
        if not get_sign(change) == direction:
            return False
    return True


data = get_data()

task1_result = task1(data)
print("Task 1:", task1_result)

task2_result = task2(data)
print("Task 2:", task2_result)