def comb(index, level):
    global choose, lst, k
    if level == 6:
        print(' '.join(choose))
        return
    for i in range(index, k):
        choose.append(lst[i])
        comb(i+1, level+1)
        choose.pop()

while True:
    case = input().split()
    if len(case) == 1:
        break
    k = int(case[0])
    choose = []
    lst = case[1:]
    comb(0,0)
    print()