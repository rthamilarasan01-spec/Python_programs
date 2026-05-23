import json


with open('word_json.json', 'r') as f:
    dictionary = json.load(f)

levels = []

for value in dictionary.values():
    levels.append(tuple(value))

level1 = levels[0]
level2 = levels[1]
level3 = levels[2]

print(level3)

# print('JSON file has been written')