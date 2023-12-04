def get_numbers(line):
    card_number, numbers = (line.split(":"))
    card_number = card_number.strip()
    card_number = int(card_number[4:].strip())
    numbers = numbers.strip()
    winning_numbers, my_numbers = numbers.split(" | ")
    return card_number, winning_numbers, my_numbers


def count_matches(winning_numbers, my_numbers):
    counter = 0
    matches = 0
    number_array = [0 for i in range(100)]
    for number in winning_numbers:
        if number != " " and number != "":
            number_array[int(number)] += 1
    for number in my_numbers:
        if number != " " and number != "": 
            if number_array[int(number)] > 0:
                if counter == 0:
                    counter += 1
                    matches += 1
                else:
                    counter *= 2
                    matches += 1
    return matches, counter

def separate_numbers(numbers):
    numbers = numbers.split(" ")
    return numbers

file = open("day_4\day_4_problem_1_input.txt", "r")
card_counter = [1 for i in range(199)]
for line in file:
    card_number, winning_numbers, my_numbers = get_numbers(line)
    winning_numbers = separate_numbers(winning_numbers)
    my_numbers = separate_numbers(my_numbers)
    # print(winning_numbers)
    # print(my_numbers)
    current_card_matches, current_card_value = count_matches(winning_numbers, my_numbers)
    print("card number: ", card_number, "matches: ", current_card_matches)
    for i in range(1, 1 + current_card_matches):
        card_counter[card_number + i] += card_counter[card_number]
    count_matches(winning_numbers, my_numbers)

sum = 0
for i in range(1, 199):
    print("card number: ", i, "card counter: ", card_counter[i])
    sum += card_counter[i]

print(sum)
