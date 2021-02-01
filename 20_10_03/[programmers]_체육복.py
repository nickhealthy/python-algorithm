n = 5
lost = [1,4]
reserve = [3]
# return 5

def solution2(n, lost, reserve):
    set_reserve = set(reserve) - set(lost)
    set_lost = set(lost) - set(reserve)
    for i in set_reserve:
        if i-1 in set_lost:
            set_lost.remove(i-1)
        elif i+1 in set_lost:
            set_lost.remove(i+1)
    return n - len(set_lost)


print(solution2(n, lost, reserve))


from itertools import cycle



def solution(n, lost, reserve):
    count = 0
    ans = [i for i in range(n)]
    for i, j, z in zip(cycle(lost), cycle(reserve), ans):
        if i+1 == j or i-1 == j:
            count += 1
    count = n - len(lost) + count
    return count


def solution1(n, lost, reserve):
    count = 0
    for i in lost:
        for j in reserve:
            if i+1 == j or i-1 == j:
                count += 1
    count = n - len(lost) + count
    return count


