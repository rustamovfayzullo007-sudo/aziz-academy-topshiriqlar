n = int(input())
a = list(map(int, input().split()))
s = 0
cnt = 0
for x in a:
    s += x
    cnt += 1
print(s / cnt)