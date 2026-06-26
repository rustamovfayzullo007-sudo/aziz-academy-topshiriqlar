yashirin_son = 20
urinish = 0
while True:
    son = int(input())
    urinish += 1
    if son == yashirin_son:
        print("Correct")
        break
    elif son < 1 or son > 20:
        print("Invalid")
    elif son < yashirin_son:
        print("Low")
    else:
        print("High")
print(urinish)