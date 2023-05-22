def solution(numbers, n):
    answer = 0
    
    for x in numbers:
        if answer > n:
            return answer
        answer += x
    
    return answer