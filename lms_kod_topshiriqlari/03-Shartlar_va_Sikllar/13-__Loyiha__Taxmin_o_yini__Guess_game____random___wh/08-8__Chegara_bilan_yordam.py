yashirin_son = 15
while True:
    son = int(input())
    farq = abs(son - yashirin_son)
    if son == yashirin_son:
        print("Correct")
        break
    elif farq >= 5:
        print("Far")
    else:
        print("Close")