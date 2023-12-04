class Number:
    def __init__(self, row, column, value, length) -> None:
        self.row = row
        self.column = column
        self.value = value
        self.length = length


    def __repr__(self) -> str:
        return f"Number({self.row}, {self.column}, {self.value}, {self.length})"


class Vector:
    def __init__(self, row, column) -> None:
        self.row = row
        self.column = column


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

def find_stars(array_1) -> list:
    stars = []
    for i in range(len(array_1)):
        for j in range(len(array_1[0])):
            if array_1[i][j] == star_symbol:
                stars.append(Vector(i, j))
    return stars


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


def validate_star(star, array):
    # counter = 0
    nums = []
    # directly above the star and below
    if array[star.row - 1][star.column].isnumeric():
        # counter += 1
        nums.append(array[star.row - 1][star.column])
    if array[star.row + 1][star.column].isnumeric():
        # counter += 1
        nums.append(array[star.row + 1][star.column])
    # directly left and right of the star
    if array[star.row][star.column - 1].isnumeric():
        # counter += 1
        nums.append(array[star.row][star.column - 1])
    if array[star.row][star.column + 1].isnumeric():
        # counter += 1
        nums.append(array[star.row][star.column + 1])
    # diagonal upper left and upper right
    if array[star.row - 1][star.column - 1].isnumeric():
        # counter += 1
        nums.append(array[star.row - 1][star.column - 1])
    if array[star.row - 1][star.column + 1].isnumeric():
        # counter += 1
        nums.append(array[star.row - 1][star.column + 1])
    # diagonal lower left and lower right
    if array[star.row + 1][star.column - 1].isnumeric():
        # counter += 1
        nums.append(array[star.row + 1][star.column - 1])
    if array[star.row + 1][star.column + 1].isnumeric():
        # counter += 1
        nums.append(array[star.row + 1][star.column + 1])
    # if counter == 2:
    #     return int(nums[0]) * int(nums[1])
    # else:
    #     print("counter: ", counter)
    #     return 0
    nums_unique = list(set(nums))
    if len(nums_unique) == 2:
        return int(nums_unique[0]) * int(nums_unique[1])
    else:
        return 0

file = open("day_3\day_3_problem_1_input.txt", "r")
symbols = "*/#=+&@%$-"
star_symbol = "*"

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


# add numbers to the array
for number in numbers:
    for i in range(number.length):
        new_array[number.row][number.column + i] = str(number.value)

print_array(new_array)


stars = find_stars(new_array)
for star in stars:
    print("star row, star column: ", star.row, star.column)


gears_sum = 0

for star in stars:
    gears_sum += validate_star(star, new_array)

print(gears_sum)


    
# print(array)