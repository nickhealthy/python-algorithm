from itertools import combinations

def isPrime(sum_nums):
    for i in range(2, int(sum_nums ** 0.5) + 1):
        if sum_nums % i == 0:
            return False
        
    return True

def solution(nums):
    result = 0

    cases = list(combinations(nums, 3))
    for case in cases:
        if isPrime(sum(case)): result += 1

    return result

print(solution([1,2,7,6,4]))