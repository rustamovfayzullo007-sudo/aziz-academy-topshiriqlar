n = int(input())
soni = 0
for i in range(1, n + 1):
    if n % i == 0:
        soni += 1
print(soni)