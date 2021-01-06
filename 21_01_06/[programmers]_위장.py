def solution(clothes):
    count = 1
    di = dict()

    for cloth in clothes:
        if cloth[1] not in di.keys():
            di[cloth[1]] = [cloth[0]]
        else:
            di[cloth[1]].append(cloth[0])

    for k in di.keys():
        count *= len(di[k]) + 1

    return count - 1
