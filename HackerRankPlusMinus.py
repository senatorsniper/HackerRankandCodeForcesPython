def plusMinus(ar):
    x = 0
    y = 0
    z = 0
    length = len(ar)
    for i in ar:
        arr = sorted(ar)
        if i < 0 :
            x += 1
        elif i > 0:
            y += 1
        else:
            z += 1
    print("{} \n{} \n{}".format(y / len(ar), x / len(ar), z / len(ar)))


n = int(input())

arr = list(map(int, input().rstrip().split()))

plusMinus(arr)
