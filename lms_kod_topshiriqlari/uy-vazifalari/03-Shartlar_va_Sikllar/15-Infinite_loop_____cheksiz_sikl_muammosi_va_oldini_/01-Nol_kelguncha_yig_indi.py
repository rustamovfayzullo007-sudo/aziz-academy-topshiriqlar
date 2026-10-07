import sys
s = 0
for n in map(int, sys.stdin.read().split()):
    if n == 0:
        break
    s += n
print(s)