n = int(input())
i = 1
yigindi = 0
while i <= n:
    if i % 2 != 0:
        yigindi += i
    i += 1
print(yigindi)