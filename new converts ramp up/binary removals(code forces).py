def binaryRemovals(st: str):
    cons1 = False
    for i in range(1, len(st)):
        if st[i] == '1' and st[i-1] == '1':
            cons1 = True
        if cons1 and (st[i] == '0' and st[i-1] == '0'):
            print('NO')
            return
    print('YES')


rep = int(input())
for _ in range(rep):
    a = input()
    binaryRemovals(a)
    
