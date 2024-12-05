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
# CORRECT AND WRONG UPDATES
correct = []
wrong = []
for update in updates:
    ok = True
    for x,y in rules:
        if x in update and y in update:
            if update.index(x) > update.index(y):
                ok = False
                break
    if ok:
        correct.append(update)
    else:
        wrong.append(update)

# print(correct)
# REORDER
reorder = []
for update in wrong:
    all_right = True
    for x,y in rules:
        if x in update and y in update:
            if update.index(x) > update.index(y):
                idx_x = update.index(x)
                idx_y = update.index(y)
                update[idx_x], update[idx_y] = update[idx_y], update[idx_x]
                wrong.append(update)
                all_right = False
                break
    if all_right:
        reorder.append(update)

# SUM OF MIDDLE
print(reorder)
result = 0
for update in reorder:
    result += update[len(update) // 2]

print(result)