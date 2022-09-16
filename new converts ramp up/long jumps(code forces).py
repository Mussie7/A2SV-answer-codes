def longJumps(n: int, a: [int]) -> int:
    ans = 0
    for i in reversed(range(n)):
        if i + a[i] < n:
            a[i] += a[a[i] + i]
        ans = max(ans, a[i])
    return ans

rep = int(input())
for _ in range(rep):
    n = int(input())
    a = list(map(int, input().split()))
    print(longJumps(n, a))
