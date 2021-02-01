'''
1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...
'''

# 풀이
from itertools import cycle

answer = [1,3,2,4,2]
a1 = [1,2,3,4,5]
a2 = [2,1,2,3,2,4,2,5]
a3 = [3,3,1,1,2,2,4,4,5,5]


def solution(answers):
    winner = []
    correct = [0, 0, 0]
    for i, j, k, z in zip(cycle(a1), cycle(a2), cycle(a3), answers):
        if i == z : correct[0] += 1
        if j == z : correct[1] += 1
        if k == z : correct[2] += 1
    
    for inx, score in enumerate(correct):
        if score == max(correct):
            winner.append(inx+1)
    
    return winner


# 다른사람 풀이
def solution1(answers):
    p = [[1, 2, 3, 4, 5],
         [2, 1, 2, 3, 2, 4, 2, 5],
         [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    s = [0] * len(p)

    for q, a in enumerate(answers):
        for i, v in enumerate(p):
            if a == v[q % len(v)]:
                s[i] += 1
    return [i + 1 for i, v in enumerate(s) if v == max(s)]
        
print(solution1(answer))
