x = int(input())
y = int(input())
z = int(input())
n = int(input())
results = []
for i in [x, range(x)]:
    for w in [y, ]:
        for l in (z, range(z)):
            if i + w + l != n:
                results.append([i, w, l])

print(sorted(results))
