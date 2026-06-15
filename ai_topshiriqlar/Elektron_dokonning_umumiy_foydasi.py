# Elektron do'konning umumiy foydasi
# Kurs: Dasturlash / IT
# Mavzu: Generator expressions
# Ball: 100
# Aziz Academy — AI Topshiriq

n = int(input())
prices = list(map(int, input().split()))
quantities = list(map(int, input().split()))
print(sum(p*q for p,q in zip(prices, quantities)))