n = int(input())
t = int(input())
soni = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if (i * j) % t == 0:
            soni += 1
print(soni)