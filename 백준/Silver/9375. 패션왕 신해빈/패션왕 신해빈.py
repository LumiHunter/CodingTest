case = int(input())

while case:
    n = int(input())
    closet = {}
    for i in range(n):
        cloth, category = input().split()
        if category not in closet.keys():
            closet[category] = []
        closet[category].append(cloth)
    ans = 1
    for _, clothes in closet.items():
        ans *= (len(clothes)+1)
    print(ans - 1)
    case -= 1