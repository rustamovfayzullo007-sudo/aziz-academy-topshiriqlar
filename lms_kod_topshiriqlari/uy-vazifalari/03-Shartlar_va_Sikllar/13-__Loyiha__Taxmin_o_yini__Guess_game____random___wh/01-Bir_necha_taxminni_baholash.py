n = int(input())
k = int(input())
for i in range(k):
    t = int(input())
    if t == n:
        print("TOPDINGIZ")
    elif t > n:
        print("KATTA")
    else:
        print("KICHIK")