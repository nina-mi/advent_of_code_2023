def get_seed_numbers(line):
    word, numbers = line.split(":")
    numbers = numbers.strip()
    return numbers.split(" ")

def get_mapping(line):
    

file = open("day_5\day_5_problem_1_input.txt", "r")
previous_line = ""
seed_numbers = []


for line in file:
    if previous_line == "":
        seed_numbers = get_seed_numbers(line)
        print(seed_numbers)
    previous_line = line