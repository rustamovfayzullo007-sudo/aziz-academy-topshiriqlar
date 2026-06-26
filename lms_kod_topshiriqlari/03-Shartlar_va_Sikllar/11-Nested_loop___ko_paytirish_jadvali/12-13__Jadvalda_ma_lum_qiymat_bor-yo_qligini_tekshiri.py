n, m = map(int, input().split())
x = int(input())
found = any(i * j == x for i in range(1, n + 1) for j in range(1, m + 1))
print("Yes" if found else "No")