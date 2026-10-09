n = int(input())
nums = list(map(int, input().split()))
print([x ** 2 for x in nums if x % 2 != 0])