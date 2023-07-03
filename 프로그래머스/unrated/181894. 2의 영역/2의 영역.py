def solution(arr):
    if 2 not in arr:
        return [-1]
    
    start = arr.index(2)
    end = start
    
    for i in range(start + 1, len(arr)):
        if arr[i] == 2:
            end = i
            
    if start == end:
        return [2]
    
    else:
        return arr[start:end + 1]
    
    return -1