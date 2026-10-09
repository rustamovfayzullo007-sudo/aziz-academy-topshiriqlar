n = int(input())
words = input().split()
print([x for x in words if len(x) >= n])