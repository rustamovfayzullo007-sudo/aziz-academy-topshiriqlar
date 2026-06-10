n = int(input())
eng_katta = 0
for i in range(1, n):
    if n % i == 0:
        eng_katta = i
print(eng_katta)