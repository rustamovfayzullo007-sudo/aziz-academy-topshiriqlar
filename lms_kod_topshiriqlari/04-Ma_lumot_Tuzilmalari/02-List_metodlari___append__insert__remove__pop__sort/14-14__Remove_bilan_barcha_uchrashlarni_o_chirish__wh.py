n = int(input())
lst = list(map(int, input().split()))
val = int(input())
while val in lst:
    lst.remove(val)
print(lst)