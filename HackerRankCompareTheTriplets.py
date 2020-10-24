def compareTriplets(a, b):
    a1 = 0
    b1 = 0
    for x in range(len(a)):
        if a[x] == b[x]:
            pass
        elif a[x] > b[x]:
            a1 += 1
        else:
            b1 += 1
    string = "{0} {1}".format(a1, b1)
    return string


a = list(map(int, input().rstrip().split()))

b = list(map(int, input().rstrip().split()))

result = compareTriplets(a, b)
print(result)
