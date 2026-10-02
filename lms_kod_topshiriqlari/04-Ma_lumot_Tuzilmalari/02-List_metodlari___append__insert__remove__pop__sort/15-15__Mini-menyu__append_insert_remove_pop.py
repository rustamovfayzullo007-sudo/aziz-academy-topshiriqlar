lst = []
while True:
    line = input().strip()
    if line == "stop":
        break
    parts = line.split()
    cmd = parts[0]
    if cmd == "append":
        lst.append(int(parts[1]))
    elif cmd == "insert":
        lst.insert(int(parts[1]), int(parts[2]))
    elif cmd == "remove":
        x = int(parts[1])
        if x in lst:
            lst.remove(x)
    elif cmd == "pop":
        idx = int(parts[1])
        if 0 <= idx < len(lst):
            lst.pop(idx)
print(lst)