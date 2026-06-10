n = int(input())
eng_kichik = 0
for i in range(2, n + 1):
    if n % i == 0:
        eng_kichik = i
        break
print(eng_kichik)