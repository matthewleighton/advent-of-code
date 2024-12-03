import re


REGEX = r"mul\((\d{1,3}),(\d{1,3})\)"

def get_data():
    with open("data.txt", "r") as f:
        return [line.rstrip() for line in f.readlines()]


def task1(data):
    total = 0
    for line in data:
        matches = re.findall(REGEX, line)
        for pair in matches:
            total += int(pair[0]) * int(pair[1])
    return total


def task2(data):
    total = 0
    enabled = True

    for line in data:
        matches = [(int(match.group(1)), int(match.group(2)), match.start()) for match in re.finditer(REGEX, line)]
        on_switches = [m.start() for m in re.finditer(r"do\(\)", line)]
        off_switches = [m.start() for m in re.finditer(r"don\'t\(\)", line)]
        for i in range(len(line)):
            if on_switches and on_switches[0] == i:
                enabled = True
                del on_switches[0]
            elif off_switches and off_switches[0] == i:
                enabled = False
                del off_switches[0]
            elif matches and matches[0][2] == i:
                if enabled:
                    total += matches[0][0] * matches[0][1]
                del matches[0]
    return total 


data = get_data()
print("Task 1:", task1(data))
print("Task 2:", task2(data))