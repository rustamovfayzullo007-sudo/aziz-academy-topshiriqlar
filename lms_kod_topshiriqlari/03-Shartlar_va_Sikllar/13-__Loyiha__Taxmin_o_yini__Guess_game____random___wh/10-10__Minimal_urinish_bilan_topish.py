yashirin_son = 1
urinish = 0
while True:
    son = int(input())
    urinish += 1
    if son == yashirin_son:
        print("Correct")
        break
    else:
        print("Try again")
print(urinish)