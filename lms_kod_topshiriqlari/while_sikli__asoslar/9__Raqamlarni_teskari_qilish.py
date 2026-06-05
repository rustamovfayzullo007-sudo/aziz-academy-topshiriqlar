n = int(input())
teskari = 0
while n > 0:
    raqam = n % 10
    teskari = teskari * 10 + raqam
    n //= 10
print(teskari)    