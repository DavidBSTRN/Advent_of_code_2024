with open("data.txt", 'r') as file:
    lines = [line.strip() for line in file.readlines()]

rules_str = []
updates_str = []
for line in lines:
    if '|' in line:  # Rules
        rules_str.append(line)
    elif ',' in line:  # Updates
        updates_str.append(line)
# RULES
rules = []
for rule in rules_str:
    x, y = map(int, rule.split('|'))
    rules.append((x, y))

# print(rules)
#UPDATES
updates = []
for update in updates_str:
    updates.append(list(map(int, update.split(','))))

# print(updates)
# CORRECT UPDATES
correct = []
for update in updates:
    ok = True
    for x,y in rules:
        if x in update and y in update:
            if update.index(x) > update.index(y):
                ok = False
                break
    if ok:
        correct.append(update)

# print(correct)
# SUM OF MIDDLE
result = 0
for update in correct:
    result += update[len(update) // 2]

print(result)


