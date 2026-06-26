n = int(input())
numbers = list(map(int, input().split()[:n]))
for x in numbers:
    if x % 2 == 0 or x < 0:
        print(x)