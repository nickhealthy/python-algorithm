def solution(common):
    one, two, three = common[:3]
    if two - one == three - two:
        return common[-1] + three - two
    else:
        return common[-1] * (three // two)
