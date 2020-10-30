def count_substring(string, sub_string):
    return string.count(sub_string)



string = input().strip()
sub_string = input().strip()

count = count_substring(string, sub_string)
print(count)