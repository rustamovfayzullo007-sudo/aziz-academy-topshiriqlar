n = int(input())
lst = list(map(int, input().split()))
x = int(input())
idx = -1
for i in range(len(lst)):
    if lst[i] == x:
        idx = i
        break
print(idx)