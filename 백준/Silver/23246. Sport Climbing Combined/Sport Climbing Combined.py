n = int(input())
lst = []
for _ in range(n):
    b, p, q, r = tuple(map(int, input().split()))
    lst.append((p*q*r, p+q+r, b))
for rank in sorted(lst)[:3]:
    print(rank[2], end=' ')