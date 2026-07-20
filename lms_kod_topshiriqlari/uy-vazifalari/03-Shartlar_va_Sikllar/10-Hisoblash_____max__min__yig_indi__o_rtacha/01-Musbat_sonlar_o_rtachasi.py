n = int(input())
yigindi = 0
boshliq_soni = 0
for _ in range(n):
    son = int(input())
    if son > 0:
        yigindi += son 
        boshliq_soni += 1
if boshliq_soni > 0:
    print(yigindi // boshliq_soni)
else:
    print(0)