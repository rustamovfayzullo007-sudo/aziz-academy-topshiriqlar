import sys
start, step = map(int, sys.stdin.read().split())
if step <= 0:
    print("CHEKSIZ")
else:
    count = 0
    while start < 100:
        start += step
        count += 1
    print(count)