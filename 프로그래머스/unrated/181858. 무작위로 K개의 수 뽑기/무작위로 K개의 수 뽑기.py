def solution(arr, k):
    answer = []
    

    
    for i in range(len(arr)):
        if arr[i] not in answer and len(answer) < k:
            answer.append(arr[i])
        
    while len(answer) < k:
        answer.append(-1)
        
    return answer