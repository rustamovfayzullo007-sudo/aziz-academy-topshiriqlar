import sys
d = list(map(int, sys.stdin.read().split()))
i, res = 0, []
while i < len(d) and (op := d[i]):
    if 1 <= op <= 6:
        a, b = d[i + 1], d[i + 2]
        i += 3
        if op in (4, 6) and b == 0:
            continue
        r = [
            a + b,
            a - b,
            a * b,
            a // b  if b else 0,
            a**b,
            a % b if b else 0,
        ][op - 1]
        print(r)
        res.append(r)
    else:
        i += 1
if res:
    print(f"Eng katta natija: {max(res)}")