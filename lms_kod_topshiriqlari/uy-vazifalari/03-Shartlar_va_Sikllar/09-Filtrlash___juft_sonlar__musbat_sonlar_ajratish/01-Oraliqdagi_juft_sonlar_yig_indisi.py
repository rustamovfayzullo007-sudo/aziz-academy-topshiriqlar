a = int(input())
b = int(input())
yigindi = 0
for son in range(a, b + 1):
    if son % 2 == 0:
        yigindi += son
print(yigindi)