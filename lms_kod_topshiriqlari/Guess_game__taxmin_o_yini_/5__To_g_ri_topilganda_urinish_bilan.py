secret = 4
tries = 0
while True:
    guess = int(input())
    tries += 1
    if guess == secret:
        print(f"Correct in {tries} tries")
        break