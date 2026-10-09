nums = [int(x) for x in input().split()]
copy = nums[:]
copy.sort()
print(*nums)
print(*copy)