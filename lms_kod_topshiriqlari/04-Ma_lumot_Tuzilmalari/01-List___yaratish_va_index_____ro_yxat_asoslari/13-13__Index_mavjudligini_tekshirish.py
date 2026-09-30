import sys
data = sys.stdin.read().split()
if len(data) > 2:
    n = int(data[0])
    lst = list(map(int, data[1:-1]))
    k = int(data[-1])
    print(lst[k] if 0 <= k < len(lst) else "Error")
else:
    print("Error")