correct  = 0

with open('advent_02.txt', 'r') as file:
    for line in file:
        vector = list(map(int, line.strip().split()))

        if vector[0] < vector[1]:
            #print(vector)
            #print(len(vector))
            #print("---------------")
            for index, value in enumerate(vector[:-1]):
                #print(index)
                if vector[index] >= vector[index + 1]:
                    break

                elif vector[index + 1] - vector[index] > 3:
                    break

                elif vector[index] < vector[index + 1] and index == len(vector)-2:
                    correct += 1

        elif vector[0] > vector[1]:
            for index, value in enumerate(vector[:-1]):
                #print(index)
                if vector[index] <= vector[index + 1]:
                    break

                elif vector[index] - vector[index + 1] > 3:
                    break

                elif vector[index] > vector[index + 1] and index == len(vector)-2:
                    correct += 1


print(correct)