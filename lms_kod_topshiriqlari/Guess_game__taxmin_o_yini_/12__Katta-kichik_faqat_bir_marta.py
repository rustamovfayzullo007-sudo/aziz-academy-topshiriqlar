yashirin_son = 8
urinish = 0
while True:
    son = int(input())
    urinish += 1
    if son == yashirin_son:
        print("Correct")
        break
    elif urinish == 1:
        if son < yashirin_son:
            print("Low")
        else:
            print("High")
    else:
        print("Wrong")
        