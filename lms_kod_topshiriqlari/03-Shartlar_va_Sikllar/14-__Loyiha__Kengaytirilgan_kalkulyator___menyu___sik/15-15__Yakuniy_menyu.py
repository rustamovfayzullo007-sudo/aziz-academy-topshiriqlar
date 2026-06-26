while True:
    line = input().split()
    if len(line) == 1 and line[0] == '0':
        print("Exit")
        break
    a, b = int(line[0]), int(line[1])
    op = int(input())
    if op == 1:
        print(a + b)
    elif op == 2:
        print(a - b)
    elif op == 3:
        print(a * b)
    elif op == 4:
        if b == 0:
            print("Error")
        else:
            print(a / b)
    elif op == 5:
        if b == 0:
            print("Error")
        else:
            print(a % b)
    elif op == 6:
        print(a ** b)    
   
