word = input()
x = 0
mo = ""
for i in word:
    if i.isupper():
        x += 1
    if x > len(word) / 2:
        mo = word.upper()
    else:
        mo = word.lower()
print(mo)