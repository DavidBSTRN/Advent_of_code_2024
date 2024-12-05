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
        if matrix[i][j] == "X":
            # XMAS
            if matrix[i][j+1] == "M" and matrix[i][j+2] == "A" and matrix[i][j+3] == "S":
                xmas_count += 1

            # SAMX
            if matrix[i][j-1] == "M" and matrix[i][j-2] == "A" and matrix[i][j-3] == "S":
                xmas_count += 1

            # UP
            if matrix[i+1][j] == "M" and matrix[i+2][j] == "A" and matrix[i+3][j] == "S":
                xmas_count += 1

            # DOWN
            if matrix[i-1][j] == "M" and matrix[i-2][j] == "A" and matrix[i-3][j] == "S":
                xmas_count += 1

            # UP RIGHT
            if matrix[i+1][j+1] == "M" and matrix[i+2][j+2] == "A" and matrix[i+3][j+3] == "S":
                xmas_count += 1

            # UP LEFT
            if matrix[i+1][j-1] == "M" and matrix[i+2][j-2] == "A" and matrix[i+3][j-3] == "S":
                xmas_count += 1

            # DOWN RIGHT
            if matrix[i-1][j+1] == "M" and matrix[i-2][j+2] == "A" and matrix[i-3][j+3] == "S":
                xmas_count += 1

            # DOWN LEFT
            if matrix[i-1][j-1] == "M" and matrix[i-2][j-2] == "A" and matrix[i-3][j-3] == "S":
                xmas_count += 1


print(xmas_count)