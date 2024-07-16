from itertools import combinations

N, S = tuple(map(int, input().split()))
nums = [i for i in map(int, input().split())]
ans = 0
for n in range(1, N + 1):
    for candidate in combinations(nums, n):
        if sum(candidate) == S:
            ans += 1
print(ans)