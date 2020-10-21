def remove(string):
    return string.replace(" ", "")


participants = 0
rangeofNumbers = input()
remove(rangeofNumbers)
rangeofNumbers = rangeofNumbers.split()
second_list = list(map(int, rangeofNumbers))
scores = input()
remove(scores)
mylist = scores.split()
mylist = list(map(int, mylist))
for x in mylist:
    if second_list[0] >= x >= second_list[1]:
        participants = participants + 1


print(participants)
