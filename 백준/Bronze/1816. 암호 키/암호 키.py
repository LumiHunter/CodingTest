N = int(input())
for i in range(N):
    num = int(input())
    for factor in range(3, 10**6, 2):
        if num % factor == 0:
            print('NO')
            break
        if factor == 10**6-1:
            print('YES')