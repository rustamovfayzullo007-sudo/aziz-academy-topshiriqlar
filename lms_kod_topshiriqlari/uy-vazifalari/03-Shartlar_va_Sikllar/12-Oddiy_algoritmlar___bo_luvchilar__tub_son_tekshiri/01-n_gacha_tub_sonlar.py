n = int(input())
natija = []
for son in range(2, n + 1):
    tub = True
    for i in range(2, son):
        if son % i == 0:
            tub = False
            break
    if tub:
        natija.append(str(son))
print(" ".join(natija))