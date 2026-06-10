n = int(input())
for num in range(2, n + 1):
    tub = True
    for i in range(2, num):
        if num % i == 0:
            tub = False
            break
    if tub:
        print(num)