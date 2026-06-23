while True:
    line = input().split()
    if len(line) == 1 and line[0] == '0':
        print("Exit")
        break       
    a, b = int(line[0]), int(line[1])
    tanlov = int(input())
    if tanlov == 1:
        print(a + b)
    elif tanlov == 2:
        print(a - b)
    elif tanlov == 3:
        print(a * b)
    elif tanlov == 4:
        print(a / b)