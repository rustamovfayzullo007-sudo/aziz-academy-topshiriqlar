import sys
items = sys.stdin.read().split()
print(*items[::-1])