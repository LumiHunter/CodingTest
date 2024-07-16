from itertools import permutations
candidates = [''.join(x) for x in permutations(['1','2','3','4','5','6','7','8','9'], 3)]
valid_candidates = candidates
N = int(input())
for _ in range(N):
    num, strike, ball = input().split()
    strike = int(strike)
    ball = int(ball)
    for index, value in enumerate(candidates):
        if not value:
            continue
        if len(set(num) & set(value)) == strike + ball:
            strike_count = 0
            for x, y in zip(num, value):
                if x == y:
                    strike_count += 1
            if strike != strike_count:
                candidates[index] = False
        else:
            candidates[index] = False

print(len(candidates)-candidates.count(False))