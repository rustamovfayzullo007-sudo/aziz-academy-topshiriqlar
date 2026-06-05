s = input()
new_s = ""
for ch in s:
    if ch == 'a':
        new_s += '@'
    else:
        new_s += ch
print(new_s)