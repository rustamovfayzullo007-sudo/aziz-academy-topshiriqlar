n = int(input())
a = list(map(int, input().split()))
s = 0
for x in a:
    s += x
avg = s / n
cnt = 0
for x in a:
    if x > avg:
        cnt += 1
print(cnt)