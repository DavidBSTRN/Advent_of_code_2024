import re

with open("data.txt", "r") as file:
    text = file.read()

# mul(a,b) do dont
pattern = r"do\(\)|don\'t\(\)|mul\(\d+,\d+\)"

matches = re.finditer(pattern, text)

order_list = []
for match in matches:
    order_list.append(match.group())

print(order_list)

add = True
useful = []

for check in order_list:
    if check == "do()":
        add = True
    elif check == "don't()":
        add = False

    if add and check != "do()":
        useful.append(check)

print(useful)

total_sum = 0

for item in useful:
    item = item[4:-1] # just nums

    a, b = map(int, item.split(','))

    total_sum += a * b


print(total_sum)