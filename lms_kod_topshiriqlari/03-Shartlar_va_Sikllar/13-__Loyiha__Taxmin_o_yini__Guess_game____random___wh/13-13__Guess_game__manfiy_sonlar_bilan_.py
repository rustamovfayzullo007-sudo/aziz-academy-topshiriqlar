yashirin_son = -4
while True:
    son = int(input())
    if son == yashirin_son:
        print("Correct")
        break
    elif son < yashirin_son:
        print("Low")
    else:
        print("High")