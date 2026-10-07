import sys
data = list(map(int, sys.stdin.read().split()))
nums = data[1 : data[0] + 1]
nums.sort()
print(*nums)