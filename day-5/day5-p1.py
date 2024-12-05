#!/usr/bin/env python3

# import re

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

    correct_updates = [update for update in listOfUpdates if is_update_in_order(update, listOfRules)]

    middle_values_sum = 0
    for update in correct_updates:
        middle_index = len(update) // 2
        middle_values_sum += update[middle_index]

    return middle_values_sum


file_path = "input1.txt"

result = getMiddleValueOfRightOrderedList(file_path)

print(f"The middle value of the right ordered list is {result}")
