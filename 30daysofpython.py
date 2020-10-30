def number(N):
    if N % 2 == 0 and 6 <= N <= 20:
        return "Weird"
    elif N % 2 == 0:
        return "Not Weird"
    else:
        return "Weird"


N = int(input())
print(number(N))