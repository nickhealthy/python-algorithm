from itertools import combinations

def solution(number):
    count = 0
    for cmb in combinations(number, 3):
        if sum(cmb) == 0:
            count += 1

    return count


