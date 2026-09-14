import sys
def solve():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    R = data[0]
    idx = 1
    rounds = []
    for i in range(1, R + 1):
        target = data[idx]
        idx += 1
        count = 0
        while True:
            guess = data[idx]
            idx += 1
            count += 1
            if guess == target:
                break
        rounds.append(count)
        print(f"Round {i}: {count} urinish")
    print(f"Jami: {sum(rounds)}")
    print(f"Eng yaxshi: {min(rounds)}")
solve()