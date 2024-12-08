import itertools

from tqdm import tqdm


def get_data():
    with open("data.txt", "r") as f:
        lines = [line.split(": ") for line in f.read().split("\n")]
    return {
        int(line[0]): [int(x)  for x in line[1].split()] for line in lines
    }


def line_is_possible(target: int , operands: list[int], include_concatenation:bool=False):
    num_operators = len(operands) - 1
    available_operators = ["+", "*"]
    if include_concatenation:
        available_operators.append("||")

    combinations = list(itertools.product(available_operators, repeat=num_operators))

    for operators in combinations:
        total = operands[0]
        for i, operand in enumerate(operands[1:]):
            if operators[i] == "+":
                total += operand
            elif operators[i] == "*":
                total *= operand
            elif operators[i] == "||":
                total = int(f"{total}{operand}")
            if total > target:
                break
        if total == target:
            return True
    return False


def task(data, include_concatenation=False):
    possible_lines = []
    for target, operands in tqdm(data.items()):
        if line_is_possible(target, operands, include_concatenation):
            possible_lines.append(target)
    return sum(possible_lines)


data = get_data()

print("Task 1:", task(data))
print("Task 2:", task(data, include_concatenation=True))