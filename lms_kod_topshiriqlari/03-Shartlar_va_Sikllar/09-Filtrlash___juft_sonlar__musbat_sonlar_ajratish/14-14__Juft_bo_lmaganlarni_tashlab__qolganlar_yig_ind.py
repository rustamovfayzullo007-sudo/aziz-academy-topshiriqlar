n = int(input())
numbers = list(map(int,input().split()))
sum_even = sum(x for x in numbers if x % 2 == 0)
print(sum_even)