import sys
data = sys.stdin.read().split()
i = 0
count = 0
total_sum = 0
while i < len(data):
    op = int(data[i])
    if op == 0:
        break
    if op in (1, 2, 3, 4):
        a = int(data[i + 1])
        b = int(data[i + 2])
        i += 3
        if op == 1:
            res = a + b
        elif op == 2:
            res = a - b
        elif op == 3:
            res = a * b
        elif op == 4:
            if b == 0:
                continue
            res = a // b
        print(res)
        count += 1
        total_sum += res
    else:
        i += 1
print(f"Amallar: {count}")
print(f"Natijalar yig'indisi: {total_sum}")