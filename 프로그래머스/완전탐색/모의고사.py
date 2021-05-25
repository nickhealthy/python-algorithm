from itertools import cycle

def solution(answers):
    first = [1,2,3,4,5]
    second = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]

    correct_cnt = [0, 0, 0]
    
    for i, j, k, ans in zip(cycle(first), cycle(second), cycle(third), answers):
        if i == ans:
            correct_cnt[0] += 1
        if j == ans:
            correct_cnt[1] += 1
        if k == ans:
            correct_cnt[2] += 1
    
    ans = [idx + 1 for idx, val in enumerate(correct_cnt) if val == max(correct_cnt)]
    return ans
            