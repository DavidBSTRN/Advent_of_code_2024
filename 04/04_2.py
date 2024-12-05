with open('data.txt', 'r') as file:
    matrix = [list(line.strip()) for line in file]
# ....xxxx...
for i, row in enumerate(matrix):
    matrix[i] = list('....') + row + list('....')

#.... up and down
row_length = len(matrix[0])  # After column padding
padding_row = list('.' * row_length)
matrix = [padding_row] * 4 + matrix + [padding_row] * 4

xmas_count = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == "A":
            # M left UP
            if matrix[i-1][j-1] == "M" and matrix[i+1][j+1] == "S":
                if matrix[i - 1][j + 1] == "M" and matrix[i + 1][j - 1] == "S":
                    xmas_count += 1

                elif matrix[i - 1][j + 1] == "S" and matrix[i + 1][j - 1] == "M":
                    xmas_count += 1

            # M right UP
            if matrix[i - 1][j + 1] == "M" and matrix[i + 1][j - 1] == "S":
                if matrix[i - 1][j - 1] == "S" and matrix[i + 1][j + 1] == "M":
                    xmas_count += 1

            # M left DONW
            if matrix[i + 1][j - 1] == "M" and matrix[i - 1][j + 1] == "S":
                if matrix[i + 1][j + 1] == "M" and matrix[i - 1][j - 1] == "S":
                    xmas_count += 1


print(xmas_count)