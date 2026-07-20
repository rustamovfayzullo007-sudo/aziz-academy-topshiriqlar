n = int(input())
sonlar = []
for _ in range(n):
    sonlar.append(int(input()))
max_qiymat = max(sonlar)
index = sonlar.index(max_qiymat) + 1
print(index)