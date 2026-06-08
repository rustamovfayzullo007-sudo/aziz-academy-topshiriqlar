n = int(input())
for i in range(n):
    print(''.join('*' if i == j else '.' for j in range(n)))