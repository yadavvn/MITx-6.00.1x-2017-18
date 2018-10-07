# Assume s is a string of lower case characters.
# Write a program that prints the number of times the string 'bob' occurs in s.

s = 'azcbobobegghakl'
count = 0

new_str = s[:]
while True:
    if 'bob' in new_str:
        count += 1
        num = new_str.index('bob')
        new_str = new_str[num+2:]
    else:
        break
    if new_str == '' or len(new_str) < 3:
        break


print("Number of times bob occurs is: {}".format(count))

