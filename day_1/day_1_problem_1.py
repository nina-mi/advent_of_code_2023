f = open("day_1_problem_1_input.txt", "r")
final_sum = 0
for x in f:
    x = x.strip()
    print(x)
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

f.close()

# f = open("file", "r") open file to read
# f = open("file", "w") open file to write, this will overwrite the file
# f = open("file", a) open file to append, this will add to the end of the file
# f = open("file", "x") create file, this will return an error if the file already exists