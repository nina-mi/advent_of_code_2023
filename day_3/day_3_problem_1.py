class Number:
    def __init__(self, row, column, value, length) -> None:
        self.row = row
        self.column = column
        self.value = value
        self.length = length


    def __repr__(self) -> str:
        return f"Number({self.row}, {self.column}, {self.value}, {self.length})"


def print_array(array_1):
    for i in range(len(array_1)):
        for j in range(len(array_1[0])):
            print(repr(array_1[i][j]), end = '')
        print()


def find_numbers(array_1) -> list:
    numbers = []
    for i in range(len(array_1)):
        current_number = ""
        for j in range(len(array_1[0])):
            if array_1[i][j] not in symbols and array_1[i][j] not in '.eud' and array_1[i][j] != '\n':
                current_number += array_1[i][j]
            elif array_1[i][j] in symbols or array_1[i][j] in '.eud' or array_1[i][j] == '\n':
                if current_number != "":
                    numbers.append(Number(i, j-len(current_number), int(current_number), len(current_number)))
                    current_number = ""

    return numbers


def validate_number(number, array):
    # before the number
    if array[number.row][number.column-1] in symbols:
        return True
    # after the number
    if array[number.row][number.column + number.length] in symbols:
        return True
    # diagonal upper left and upper right
    if array[number.row - 1][number.column - 1] in symbols or array[number.row - 1][number.column + number.length] in symbols:
        return True
    # diagonal lower left and lower right
    if array[number.row + 1][number.column - 1] in symbols or array[number.row + 1][number.column + number.length] in symbols:
        return True
    # directly above the number and below
    for i in range(number.length):
        if array[number.row - 1][number.column + i] in symbols:
            return True
        if array[number.row + 1][number.column + i] in symbols:
            return True
    return False

file = open("day_3\day_3_problem_1_input.txt", "r")
symbols = "*/#=+&@%$-"

array = []
i = 0

for line in file:
    array.append([])
    array[i] = ['e'] + [j for j in line]
    i += 1

new_array = [['u' for i in range(len(array[0]))]] + array + [['d' for i in range(len(array[0]))]]
# print(new_array)
# print_array(new_array)
numbers = find_numbers(new_array)

sum = 0
for num in numbers:
    if validate_number(num, new_array):
        sum += num.value

print(sum)

    
# print(array)