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

distance = 0

for i in range(len(list1)):
    minimum_A = min(list1)
    minimum_B = min(list2)

    index_A = list1.index(minimum_A)
    index_B = list2.index(minimum_B)

    distance += abs(minimum_B - minimum_A)

    del list1[index_A]
    del list2[index_B]

print(distance)