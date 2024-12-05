#!/usr/bin/env python3


def getMiddleValueOfRightOrderedList(filePath):
    listOfUpdates = []
    listOfRules = []
    with open(filePath, 'r') as file:
        lines = file.readlines()

    parsing_rules = True
    for line in lines:
        if line.strip() == "":
            parsing_rules = False
            continue
        if parsing_rules:
            listOfRules.append(tuple(map(int, line.strip().split('|'))))
        else:
            listOfUpdates.append(list(map(int, line.strip().split(','))))

    def is_update_in_order(update, rules):
        for a, b in rules:
            if a in update and b in update:
                if update.index(a) > update.index(b):
                    return False
        return True

    def order_update(update, rules):
        ordered_update = update[:]
        for a, b in sorted(rules, key=lambda x: (update.index(x[0]) if x[0] in update else float('inf'), update.index(x[1]) if x[1] in update else float('inf'))):
            if a in ordered_update and b in ordered_update:
                a_index = ordered_update.index(a)
                b_index = ordered_update.index(b)
                if a_index > b_index:
                    ordered_update.remove(a)
                    ordered_update.insert(b_index, a)
        return ordered_update

    incorrect_updates = [update for update in listOfUpdates if not is_update_in_order(update, listOfRules)]

    corrected_updates = [order_update(update, listOfRules) for update in incorrect_updates]

    middle_values_sum = 0
    for update in corrected_updates:
        middle_index = len(update) // 2
        middle_values_sum += update[middle_index]

    return middle_values_sum


file_path = "input1.txt"

result = getMiddleValueOfRightOrderedList(file_path)

print(f"The middle value is {result}")
