import sys
data = list(map(int, sys.stdin.read().split()))
idx = 0
while idx < len(data):
    op = data[idx]
    idx += 1
    if op == 0:
        break
    a = data[idx]
    b = data[idx + 1]
    idx += 2
    if op == 1:
        print(a + b)
    elif op == 2:
        print(a - b)
    elif op == 3:
        print(a * b)
    elif op == 4:
        print("Xato" if b == 0 else a // b)
    else:
        print("Noma'lum")