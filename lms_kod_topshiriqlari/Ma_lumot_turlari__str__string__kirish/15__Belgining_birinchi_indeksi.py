s = input()
ch = input()
s_sorted = sorted(s)
print(s_sorted.index(ch) if ch in s_sorted else -1)