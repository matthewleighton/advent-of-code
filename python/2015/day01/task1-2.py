def get_data():
    with open("data.txt") as file:
        return file.readline().rstrip()


def tasks(data):
    floor = 0
    entered_basement = False
    commands = {"(": 1, ")": -1}

    for i, character in enumerate(data):
        floor += commands[character]

        if not entered_basement and floor < 0:
            entered_basement = i + 1

    return floor, entered_basement


data = get_data()
floor, entered_basement = tasks(data)

print(f"Task 1: {floor}")
print(f"Task 2: {entered_basement}")
