n = int(input())
nums = list(map(int, input().split()))
print([x * 10 for x in nums if x % 2 == 0])