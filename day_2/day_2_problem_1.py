file = open("day_2\day_2_problem_1_input.txt", "r")
sum = 0

# the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes
allowed_R = 12
allowed_G = 13
allowed_B = 14

for x in file:
    x = x.replace("red", "R")
    x = x.replace("blue", "B")
    x = x.replace("green", "G")
    first_split = x.split(":")
    id = (first_split[0].split(" "))[1] # this works to get the game id
    print("Game id: ", id)
    bool = True
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
                if number > allowed_R:
                    bool = False
                    break
            elif tiny_part[-1] == "G":
                print("hello2")
                if number > allowed_G:
                    bool = False
                    break
            elif tiny_part[-1] == "B":
                print("hello3")
                print(number, allowed_B)
                if number > allowed_B:
                    bool = False
                    break
    if bool == True:
        sum += int(id)

    print(sum)

print(sum)

