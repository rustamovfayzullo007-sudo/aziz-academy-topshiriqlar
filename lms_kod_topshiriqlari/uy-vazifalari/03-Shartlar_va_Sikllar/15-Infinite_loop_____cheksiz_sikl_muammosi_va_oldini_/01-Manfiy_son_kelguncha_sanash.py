import sys
count = 0
for n in map(int, sys.stdin.read().split()):
    if n < 0:
        break
    count += 1
print(count)