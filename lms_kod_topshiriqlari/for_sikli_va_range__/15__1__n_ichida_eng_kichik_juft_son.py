
n = int(input())
ans = None
for i in range(1, n + 1):
    if i % 2 == 0:
        ans = i
        break
if ans is None:
    print("No")
else:
    print(ans)