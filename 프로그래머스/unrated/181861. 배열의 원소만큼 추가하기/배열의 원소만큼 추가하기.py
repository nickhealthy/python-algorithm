def solution(arr):
    answer = []
    
    for elem in arr:
        answer += [elem] * elem
    
    return answer