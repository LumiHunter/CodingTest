def solution(food):
    answer = ''
    for f, num in enumerate(food):
        share = num // 2
        if share == 0:
            continue
        for i in range(share):
            answer = answer + str(f)
    answer = answer + '0' + answer[::-1]
    return answer