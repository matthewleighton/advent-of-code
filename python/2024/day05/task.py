def get_data():
    with open("data.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]
    break_index = lines.index("")
    rules = []
    print_orders = []
    for i, line in enumerate(lines):
        if i < break_index:
            rules.append(line.split("|"))
        elif i > break_index:
            print_orders.append(line.split(","))
    return rules, print_orders
    
    
def task1(rules, print_orders):
    valid_orders = [
        order for order in print_orders if is_order_valid(order, rules)
    ]
    return sum_middle_numbers(valid_orders)


def task2(rules, print_orders):
    invalid_orders = [
        order for order in print_orders if not is_order_valid(order, rules)
    ]
    fixed_orders = [
        fix_order(order, rules) for order in invalid_orders
    ]
    return sum_middle_numbers(fixed_orders)


def is_order_valid(order, rules):
    for page_number in order:
        relevant_rules = [rule for rule in rules if page_number in rule]
        for rule in relevant_rules:
            rule_index_target = rule.index(page_number)
            rule_index_other = int(not bool(rule_index_target))
            if rule[rule_index_other] not in order:
                continue
            order_index_other = order.index(rule[rule_index_other])
            order_index_target = order.index(page_number)
            if rule_index_target < rule_index_other and order_index_target > order_index_other:
                return False
            if rule_index_target > rule_index_other and order_index_target < order_index_other:
                return False
    return True

def fix_order(original_order, rules):
    new_order = [original_order[0]]
    for page_number in original_order[1:]:
        placement_index = 0
        for element in new_order:
            relevant_rule = [
                rule for rule in rules if page_number in rule and element in rule
            ][0]
            if relevant_rule.index(page_number) > relevant_rule.index(element):
                placement_index += 1
        new_order.insert(placement_index, page_number)
    return new_order


def sum_middle_numbers(orders):
    return sum([
        int(order[int(len(order)/2)])
        for order in orders
    ])


rules, print_orders = get_data()

print("Task 1:", task1(rules, print_orders))
print("Task 2:", task2(rules, print_orders))