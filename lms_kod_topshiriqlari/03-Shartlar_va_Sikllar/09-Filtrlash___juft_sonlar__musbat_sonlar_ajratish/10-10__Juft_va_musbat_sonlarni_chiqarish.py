n = int(input())
a = list(map(int, input().split()))
for x in a:
    if x > 0 and x % 2 == 0:
        print(x)