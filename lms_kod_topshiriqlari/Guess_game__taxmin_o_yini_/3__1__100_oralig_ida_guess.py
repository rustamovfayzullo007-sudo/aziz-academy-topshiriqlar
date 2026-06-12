secret = 42
while True:
    trt:
        line = input()
        if not line:
            break
        guess = int(line)
        if guess < secret:
            print("Low")
        elif guess > secret:
            print("High")
        else:
            print("Correct")
            break
        