def sol(n):
    if n == 0:
        return('-')
    return(sol(n-1) + ' ' * pow(3,(n-1)) + sol(n-1))

while True:
    try:
        N = int(input())
        print(sol(N))
    except:
        break