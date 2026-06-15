secret = 8
attempts = 3
for i in range(attempts):
    try:
        guess = int(input())
        if guess == secret:
            print("Correct")
            break
        if i == attempts - 1:
            print("Game Over")
    except ValueError:
        continue
       