import sys 
def solve():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    target = data[0]
    score = 100
    for x in data[1:]:
        if x > target:
            print("KATTA")
            score = max(0, score - 10)
        elif x < target:
            print("KICHIK")
            score = max(0, score - 10)
        else:
            print("TOPDINGIZ")
            print(f"Ball: {score}")
            break
solve()