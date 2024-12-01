import csv

# Replace 'your_file.csv' with the path to your CSV file
file_path = '01_input.csv'

list1 = []
list2 = []

with open(file_path, 'r', encoding='utf-8-sig') as file:
    reader = csv.reader(file, delimiter=';')  # Specify the semicolon delimiter
    for row in reader:
        list1.append(row[0])  # First column
        list2.append(row[1])  # Second column

list1 = [int(x) for x in list1]
list2 = [int(x) for x in list2]

similarity = 0

for index_1, value_1 in enumerate(list1):
    for index_2, value_2 in enumerate(list2):
        if value_1 == value_2:
            similarity += value_1

print(similarity)