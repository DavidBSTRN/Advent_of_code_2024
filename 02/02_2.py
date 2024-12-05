def check_vector(vector):

    if vector[0] < vector[1]:
        for index in range(len(vector) - 1):
            if vector[index] >= vector[index + 1] or abs(vector[index] - vector[index + 1]) > 3:
                return False
        return True

    elif vector[0] > vector[1]:
        for index in range(len(vector) - 1):
            if vector[index] <= vector[index + 1] or abs(vector[index] - vector[index + 1]) > 3:
                return False
        return True

    return False


def second_chance(vector):

    for i in range(len(vector)):
        modified_vector = vector[:i] + vector[i + 1:]
        if check_vector(modified_vector):
            return True
    return False


if __name__ == "__main__":
    correct = 0
    wrong_ones = []
    with open('advent_02.txt', 'r') as file:
        for line in file:
            vector = list(map(int, line.strip().split()))

            result = check_vector(vector)
            if result is True:
                correct += 1
            else:
                wrong_ones.append(vector)

    print(correct)

    for wrong in wrong_ones:
        if second_chance(wrong):
            correct += 1

    print(correct)
