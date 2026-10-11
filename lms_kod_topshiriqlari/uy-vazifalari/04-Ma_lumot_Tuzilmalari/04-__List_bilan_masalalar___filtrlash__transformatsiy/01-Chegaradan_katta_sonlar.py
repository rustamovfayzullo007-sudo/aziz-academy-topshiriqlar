sonlar = map(int, input().split())
t = int(input())
print(*(x for x in sonlar if x > t))
