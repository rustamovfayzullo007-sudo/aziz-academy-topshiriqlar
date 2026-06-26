a, b = map(int, input().split())
op = input()
if op == "add":
    print(a + b)
elif op == "sub":
    print(a - b)
elif op == "mul":
    print(a * b)
elif op == "div":
    if b == 0:
        print("Error")
    else:
        print(a / b)
