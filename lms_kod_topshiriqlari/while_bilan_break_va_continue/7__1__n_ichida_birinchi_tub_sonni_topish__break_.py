n = int(input())
if n < 2:
    print("No")
else:
    i = 2
    while i <= n:
        tub = True
        j = 2
        while j < i:
            if i % j == 0:
                tub = False
                break
            j += 1
        if tub:
            print(i)
            break
        i += 1