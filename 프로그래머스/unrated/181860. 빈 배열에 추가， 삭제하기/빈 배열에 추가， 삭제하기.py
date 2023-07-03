def solution(arr, flag):
    answer = []
    
    for elem, isTrue in zip(arr, flag):
        if isTrue:
            answer += [elem] * elem * 2
            continue
            
        answer = answer[:-elem]
        
    
    return answer