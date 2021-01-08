# from itertools import cycle
# 가장 긴 리스트를 기준으로 "반복", "순회" 해줌


# 예시
from itertools import cycle

def solution(answers):
    a1 = [1,2,3,4,5]
    a2 = [2,1,2,3,2,4,2,5]
    a3 = [3,3,1,1,2,2,4,4,5,5]
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