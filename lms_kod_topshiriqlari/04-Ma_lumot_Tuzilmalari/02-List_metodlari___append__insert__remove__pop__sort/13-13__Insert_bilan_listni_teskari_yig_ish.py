n = int(input())
nums = map(int, input().split())
lst = []
for x in nums:
    lst.insert(0, x)
print(lst)