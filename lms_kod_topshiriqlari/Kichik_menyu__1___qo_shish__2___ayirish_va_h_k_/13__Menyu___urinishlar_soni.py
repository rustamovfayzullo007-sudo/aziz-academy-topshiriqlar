count = 0
while True:
    line = input().split()
    if len(line) == 1 and line[0] == '0':
        print(count)
        break
    a, b = int(line[0]), int(line[1])
    tanlov = int(input())
    count += 1