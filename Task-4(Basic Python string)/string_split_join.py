# You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

a = line.split(" ")
    a = "-".join(a)
    return a

line = input()
result = split_and_join(line)
print(result)