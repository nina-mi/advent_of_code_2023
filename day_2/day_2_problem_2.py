file = open("day_2\day_2_problem_1_input.txt", "r")
sum = 0


for x in file:
    b = 0
    g = 0
    r = 0

    x = x.replace("red", "R")
    x = x.replace("blue", "B")
    x = x.replace("green", "G")
    first_split = x.split(":")
    id = (first_split[0].split(" "))[1] # this works to get the game id
    print("Game id: ", id)
    parts = first_split[1].split(";")
    
    for part in parts:
        tiny_parts = (part.strip()).split(",")
        print(tiny_parts)
        for tiny_part in tiny_parts:
            tiny_part = tiny_part.strip()
            space_index = tiny_part.find(" ")
            number = int(tiny_part[0:space_index+1])
            print(number)
            print(tiny_part[-1])
            print("\n")
            if tiny_part[-1] == "R":
                print("hello1")
                if number > r:
                    r = number
            elif tiny_part[-1] == "G":
                print("hello2")
                if number > g:
                    g = number
            elif tiny_part[-1] == "B":
                print("hello3")
                if number > b:
                    b = number
        
    sum += b*g*r

    print(sum)

print(sum)

# REGEX solution:
# import re, math

# def f(line):
#     bag = {'r':0, 'g':0, 'b':0}
#     for num, col in re.findall(r'(\d+) (\w)', line):
#         bag[col] = max(bag[col], int(num))
#     return math.prod(bag.values())

