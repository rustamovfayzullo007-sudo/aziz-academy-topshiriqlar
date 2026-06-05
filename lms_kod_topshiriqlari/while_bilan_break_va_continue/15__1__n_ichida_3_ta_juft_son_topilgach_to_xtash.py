n = int(input())
i = 1
s = 0
while i <= n:
    if i % 2 == 0:
        s += 1
    if s == 3:
        print(i)
        break
    i += 1
if s < 3:
    print("No")
