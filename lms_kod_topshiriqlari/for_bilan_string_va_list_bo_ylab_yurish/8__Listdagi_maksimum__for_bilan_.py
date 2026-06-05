n = int(input())
a = list(map(int, input().split()))
eng_katta = a[0]
for i in range(1, n):
    if a[i] > eng_katta:
        eng_katta = a[i]
print(eng_katta)