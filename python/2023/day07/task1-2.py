CARD_LABELS_1 = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
CARD_LABELS_2 = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]


def get_data(filename):
    with open(filename) as f:
        hands = [line.rstrip().split(" ") for line in f.readlines()]
    for hand in hands:
        hand[1] = int(hand[1])
    return hands


def get_hand_type(hand_cards, task=1):
    card_counts = get_card_counts(hand_cards)
    if task == 2:
        joker_count = card_counts.get("J", 0)
        card_counts["J"] = 0
        card_counts[max(card_counts, key=card_counts.get)] += joker_count
    count_amounts = sorted(list(card_counts.values()))

    if count_amounts[-1] == 5:
        return 1
    if count_amounts[-1] == 4:
        return 2
    if count_amounts[-1] == 3:
        if count_amounts[-2] == 2:
            return 3
        return 4
    if count_amounts[-1] == 2:
        if count_amounts[-2] == 2:
            return 5
        return 6
    return 7


def get_card_counts(hand_cards):
    card_counts = {}
    for card in hand_cards:
        if card in card_counts:
            card_counts[card] += 1
        else:
            card_counts[card] = 1
    return card_counts


def count_unique_labels(hand_cards):
    num = 0
    found_labels = []
    for card in hand_cards:
        if card not in found_labels:
            found_labels.append(card)
            num += 1
    return num


def task_1_sort(hand):
    return sort_hands(hand, CARD_LABELS_1)


def task_2_sort(hand):
    return sort_hands(hand, CARD_LABELS_2)


def sort_hands(hand, labels_order):
    return [hand[2]] + [labels_order.index(hand[0][i]) for i in range(len(hand[0]))]


def assign_hand_types(data, task=1):
    data_with_types = []
    for hand in data:
        data_with_types.append(hand + [get_hand_type(hand[0], task)])
    sort_func = {1: task_1_sort, 2: task_2_sort}[task]
    data_with_types.sort(key=sort_func, reverse=True)
    return data_with_types


def get_hand_score(data):
    score = 0
    for i, hand in enumerate(data):
        score += (i + 1) * hand[1]
    return score


def task_1(data):
    data = assign_hand_types(data)
    return get_hand_score(data)


def task_2(data):
    data = assign_hand_types(data, task=2)
    return get_hand_score(data)


data = get_data("data.txt")


task_1_result = task_1(data)
print("Task 1: ", task_1_result)

task_2_result = task_2(data)
print("Task 2: ", task_2_result)
