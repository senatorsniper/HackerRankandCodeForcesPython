x = 0
a, b = input().split()
a = int(a)
b = int(b)
while b >= a:
    a *= 3
    b *= 2
    x += 1
print(x)
