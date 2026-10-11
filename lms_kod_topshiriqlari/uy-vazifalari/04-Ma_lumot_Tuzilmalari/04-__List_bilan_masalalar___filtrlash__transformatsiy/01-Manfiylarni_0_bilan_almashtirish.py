sonlar = [x if x >= 0 else 0 for x in map(int, input().split())]
print(*sonlar)