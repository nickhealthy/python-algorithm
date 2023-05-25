def solution(rank, attendance):
    tmp = {}
    for idx, val in enumerate(rank):
        if attendance[idx]:
            tmp[val] = idx

    tmp = sorted(tmp.items())[:3]
    answer = 10000 * tmp[0][1] + 100 * tmp[1][1] + tmp[2][1]
    return answer