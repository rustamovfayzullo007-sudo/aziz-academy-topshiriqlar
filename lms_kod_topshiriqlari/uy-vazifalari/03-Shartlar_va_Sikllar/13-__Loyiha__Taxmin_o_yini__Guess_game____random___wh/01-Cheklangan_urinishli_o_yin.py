son = int(input())
n = int(input())
topdi = False
for i in range(n):
    taxmin = int(input())
    if taxmin == son:
        print("TOPDINGIZ")
        topdi = True
        break
    elif taxmin > son:
        print("KATTA")
    else:
        print("KICHIK")
if not topdi:
    print("YUTQAZDINGIZ")