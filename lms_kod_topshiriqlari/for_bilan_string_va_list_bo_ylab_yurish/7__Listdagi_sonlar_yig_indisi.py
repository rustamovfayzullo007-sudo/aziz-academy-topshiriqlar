n = int(input())
a = list(map(int, input().split()))
summa = 0
for i in range(n):
    summa += a[i]
print(summa)