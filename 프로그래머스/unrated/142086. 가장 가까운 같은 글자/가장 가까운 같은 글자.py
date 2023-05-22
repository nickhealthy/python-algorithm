def solution(s):
    answer = []

    tmp = []
    for idx, val in enumerate(s):
        if val not in tmp:
            tmp.append(val)
            answer.append(-1)

        elif val in tmp:
            element = abs(idx - len(tmp) - tmp[::-1].index(val) - 1)
            tmp.append(val)
            answer.append(element)

    return answer