n = int(input())
nums = list(map(int, input().split()))
print([x for x in nums if 0 < x < 100])