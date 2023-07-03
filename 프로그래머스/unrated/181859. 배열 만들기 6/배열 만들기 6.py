def solution(arr):
    answer = []
    
    i = 0
    end = len(arr)
    while i < end:
        if not answer:
            answer.append(arr[i])
            i += 1

        elif answer and answer[-1] == arr[i]:
            answer.pop()
            i += 1
        
        elif answer and answer[-1] != arr[i]:
            answer.append(arr[i])
            i += 1
    
    if answer:
        return answer
    
    return [-1]