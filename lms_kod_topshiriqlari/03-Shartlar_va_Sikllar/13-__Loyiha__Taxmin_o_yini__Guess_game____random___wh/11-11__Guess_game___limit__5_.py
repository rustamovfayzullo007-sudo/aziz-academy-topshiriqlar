yashirin_son = 10
topildi = False
for i in range(5):
    son = int(input())
    if son == yashirin_son:
        topildi = True
        break
if topildi:
    print("Correct")
else:
    print("You lost")