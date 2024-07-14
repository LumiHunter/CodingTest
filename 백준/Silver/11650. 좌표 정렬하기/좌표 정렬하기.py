N = int(input())
lst = [tuple(map(int, input().split())) for _ in range(N)]
for x, y in sorted(lst):
    print(x, y)