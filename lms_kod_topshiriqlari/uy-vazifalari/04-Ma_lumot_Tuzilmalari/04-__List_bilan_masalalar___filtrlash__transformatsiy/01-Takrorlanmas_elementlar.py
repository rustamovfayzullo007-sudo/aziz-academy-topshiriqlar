res = []
for x in input().split():
    if x not in res:
        res.append(x)
print(*res)
