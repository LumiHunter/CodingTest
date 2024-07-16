from itertools import permutations

def is_lucky(string):
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            return False
    return True

S = input()
if len(S) == 1:
    print(1)
elif len(S) == 2:
    print(int(S[0] != S[1]) * 2)
else:
    ans = set()
    for string in permutations(S,len(S)):
        if is_lucky(string):
            ans.add(''.join(string))
    print(len(ans))