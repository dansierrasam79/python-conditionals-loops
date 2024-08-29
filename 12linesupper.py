# lines in upper case
lines = []
l = " "
while len(l) > 0:
    l = input("Enter word or line: ")
    if l:
        lines.append(l.upper())
print(lines)