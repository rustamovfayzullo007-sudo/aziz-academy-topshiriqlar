yashirin_son = 3
while True:
    son = int(input())
    if son == 0:
        print("Exit")
        break
    elif son == yashirin_son:
        print("Correct")
        break
    elif son < yashirin_son:
        print("Low")
    else:
        print("High")