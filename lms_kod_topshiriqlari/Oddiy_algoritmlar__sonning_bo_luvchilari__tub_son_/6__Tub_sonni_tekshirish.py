n = int(input())
if n <= 1:
    print("Composite")
else:
    tub = True
    for i in range(2, n):
        if n % i == 0:
            tub = False
            break
    if tub:
        print("Prime")
    else:
        print("Composite")