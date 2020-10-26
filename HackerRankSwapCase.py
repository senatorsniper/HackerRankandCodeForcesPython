def swap_case(s):
    x = 0
    string = ''
    second_list = []
    my_list = list(map(str, s))
    for i in my_list:
        if i.isupper():
            second_list.append(i.lower())
        else:
            second_list.append(i.upper())
    string = string.join(second_list)
    return string


s = input()
print(swap_case(s))