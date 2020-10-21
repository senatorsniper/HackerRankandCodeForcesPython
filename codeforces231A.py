def remove(string):
    return string.replace(" ", "")

number = 0
numberofinputs = int(input())
my_list = []
for x in range(numberofinputs):
    input1 = input()
    input1 = remove(input1)
    second_list = list(map(int, input1))
    my_list.append(second_list)
for x in range(len(my_list)):
    if my_list[x][0] + my_list[x][1] + my_list[x][2] >= 2:
        number = number + 1

print(int(number))



