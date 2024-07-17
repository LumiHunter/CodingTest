N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = 0
for a in sorted(A):
    b = max(B)
    ans += a*b
    B.remove(b) 
print(ans)