def aVeryBigSum(arr):
    sum1 = 0
    for num in arr:
        sum1 += num
    return sum1


ar_count = int(input())
ar = list(map(int, input().rstrip().split()))
result = aVeryBigSum(ar)
print(result)
