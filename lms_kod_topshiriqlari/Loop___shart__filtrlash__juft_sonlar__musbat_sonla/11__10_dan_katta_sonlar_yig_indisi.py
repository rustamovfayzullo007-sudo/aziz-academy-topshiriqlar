n = int(input())
a = list(map(int, input().split()))
s = 0
for x in a:
    if x > 10:
        s += x
print(s)