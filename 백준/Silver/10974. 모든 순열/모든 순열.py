from itertools import permutations

N = int(input())
for permutation in list(permutations(range(1,N+1))):
    print(' '.join(list(map(str,permutation))))