son = int(input())
urinish = 0
while True:
    taxmin = int(input())
    urinish += 1
    if taxmin == son:
        print("TOPDINGIZ")
        break
    elif taxmin > son:
        print("KATTA")
    else:
        print("KICHIK")
print("Urinishlar:", urinish)
                 