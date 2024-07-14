N = int(input())
lst = []
for _ in range(N):
    lst.append(tuple(map(int,input().split())))
for t in sorted(lst):
    print(' '.join(list(map(str, t))))