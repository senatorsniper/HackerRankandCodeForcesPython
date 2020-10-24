def simpleArraySum(ar):
    sum1 = 0
    for i in ar:
        sum1 += i
    return sum1


ar_count = int(input())
ar = list(map(int, input().rstrip().split()))

print(simpleArraySum(ar))
