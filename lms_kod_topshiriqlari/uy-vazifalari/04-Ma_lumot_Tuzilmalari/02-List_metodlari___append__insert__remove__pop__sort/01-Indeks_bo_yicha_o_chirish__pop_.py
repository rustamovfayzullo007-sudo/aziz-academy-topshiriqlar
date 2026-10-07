import sys
data = sys.stdin.read().split()
k = int(data.pop())
data.pop(k)
print(*data)