n = int(input())
a = list(map(int, input().split()))
k = int(input())
best = a[0]
for x in a:
    if abs(x - k) < abs(best - k):
        best = x
    elif abs(x - k) == abs(best - k) and x < best:
        best = x
print(best)