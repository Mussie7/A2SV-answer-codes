def strangeBDParty(n: int, m: int, k: [int], c: [int]) -> int:
    k.sort(reverse=True)
    cost = l = 0
    for i in range(n):
        if l < m and c[l] < c[k[i] - 1]:
            cost += c[l]
            l += 1
        else:
            cost += c[k[i] - 1]
    
    return cost

rep = int(input())
for _ in range(rep):
    n, m = list(map(int, input().split()))
    k = list(map(int, input().split()))
    c = list(map(int, input().split()))
    print(strangeBDParty(n, m, k, c))
