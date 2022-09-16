def dogWalks(n: int, k: int, a: [int]):
    walks = 0
    for i in range(n - 1):
        if a[i] + a[i+1] < k:
            walks += k - (a[i] + a[i+1])
            a[i+1] += k - (a[i] + a[i+1])
    
    print(walks)
    for i in range(n-1):
        print(str(a[i]), end = " ")
    print(str(a[-1]))


n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
dogWalks(n, k, a)
