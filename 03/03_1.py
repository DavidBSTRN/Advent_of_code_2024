import re

with open("data.txt", "r") as file:
    text = file.read()

# mul(a,b)
pattern = r"(?<!\w)mul\((\d+),(\d+)\)"

matches = re.findall(pattern, text)

result = 0
for couple in matches:
    result += int(couple[0]) * int(couple[1])

print(result)