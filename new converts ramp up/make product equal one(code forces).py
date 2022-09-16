n = int(input())
a = list(map(int, input().split()))
neg = coins = 0
zeroes = False
for i in range(n):
    if a[i] < 0:
        neg += 1
    
    if a[i]:
        coins += abs(a[i]) - 1
    else:
        zeroes = True
        coins += 1

if neg % 2 and not zeroes:
    coins += 2

print(coins)
