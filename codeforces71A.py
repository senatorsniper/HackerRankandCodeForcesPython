numberofLines = int(input())
my_list = []
for x in range(numberofLines):
    word = input()
    wordLength = len(word)
    word1 = wordLength - 2
    word1 = str(word1)
    if wordLength > 10:
        firstChar = word[0]
        lastChar = word[wordLength - 1]
        my_list.append(firstChar + word1 + lastChar)
    else:
        my_list.append(word)
for a in range(len(my_list)):
    print(my_list[a])
