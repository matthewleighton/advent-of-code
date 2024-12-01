def get_data():
    with open("data.txt", "r") as f:
        lines = [line.rstrip().split("   ") for line in f.readlines()]
    return [
        sorted([int(d[i]) for d in lines])
        for i in [0, 1]
    ]

def task1(data):
    total = 0
    for i in range(len(data[0])):
        total += abs(data[0][i] - data[1][i])
    return total

def task2(data):
    total = 0
    for left_number in data[0]:
        total += left_number * data[1].count(left_number)
    return total

data = get_data()
print("Task 1:", task1(data))
print("Task 2:", task2(data))