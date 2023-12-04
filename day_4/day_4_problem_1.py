def get_numbers(line):
    card_number, numbers = (line.split(":"))
    card_number = card_number.strip()
    numbers = numbers.strip()
    winning_numbers, my_numbers = numbers.split(" | ")
    return winning_numbers, my_numbers


def count_matches(winning_numbers, my_numbers):
    counter = 0
    number_array = [0 for i in range(100)]
    for number in winning_numbers:
        if number != " " and number != "":
            number_array[int(number)] += 1
    for number in my_numbers:
        if number != " " and number != "": 
            if number_array[int(number)] > 0:
                if counter == 0:
                    counter += 1
                else:
                    counter *= 2
    return counter

def separate_numbers(numbers):
    numbers = numbers.split(" ")
    return numbers

file = open("day_4\day_4_problem_1_input.txt", "r")
sum = 0
for line in file:
    winning_numbers, my_numbers = get_numbers(line)
    winning_numbers = separate_numbers(winning_numbers)
    my_numbers = separate_numbers(my_numbers)
    # print(winning_numbers)
    # print(my_numbers)
    sum += count_matches(winning_numbers, my_numbers)

print(sum)
