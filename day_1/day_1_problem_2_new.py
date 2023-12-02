def turn_into_numbers(x):
    x = x.replace("one", "o1e")
    x = x.replace("two", "t2o")
    x = x.replace("three", "t3e")
    x = x.replace("four", "f4r")
    x = x.replace("five", "f5e")
    x = x.replace("six", "s6x")
    x = x.replace("seven", "s7n")
    x = x.replace("eight", "e8t")
    x = x.replace("nine", "n9e")
    return x

f = open("day_1_problem_1_input.txt", "r")
final_sum = 0
for x in f:
    x = x.strip()
    print(x)
    x = turn_into_numbers(x)
    first_digit = None
    last_digit = None
    for i in x:
        if i in "0123456789":
            first_digit = i
            break
    print(first_digit)
    for i in range(len(x)-1, -1, -1):
        if x[i] in "0123456789":
            last_digit = x[i]
            break
    print(last_digit)
    sum = str(first_digit) + str(last_digit)
    print(sum)
    final_sum += int(sum)
print(final_sum)