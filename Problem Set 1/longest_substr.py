# Assume s is a string of lower case characters.
# Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
# In the case of ties, print the first substring

s = 'azcbobobegghakl'
# s = 'abcbcd'

compare_str = ' '
final_str = ''
length = 0
for letter in s:
    if letter >= compare_str[-1]:
        if compare_str[-1] == ' ':
            compare_str = letter
        else:
            compare_str += letter
    else:
        compare_str = letter

    if len(compare_str) > length:
        final_str = compare_str
        length = len(compare_str)

print("Longest substring in alphabetical order is: {}".format(final_str))
