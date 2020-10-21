x = list(map(int, input().rstrip().split()))
y = x[2] + 1
number = 0
for i in range(y):
    number += i * x[0]
number -= x[1]
if number <= 0:
    number = 0
print(number)
