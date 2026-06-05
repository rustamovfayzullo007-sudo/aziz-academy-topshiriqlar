soni = 0 
while True:
    son = int(input())
    if son == 0:
        break
    if son < 0:
        continue
    soni += 1
print(soni)