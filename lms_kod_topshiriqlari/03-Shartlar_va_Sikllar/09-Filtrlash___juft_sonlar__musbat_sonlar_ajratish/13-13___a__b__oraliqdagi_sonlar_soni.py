n = int(input())
a_list = list(map(int, input().split()))
a, b = map(int, input().split())
cnt = 0
for x in a_list:
    if a <= x <= b:
        cnt += 1
print(cnt)