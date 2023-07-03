def solution(arr1, arr2):
    l_arr1 = len(arr1)
    l_arr2 = len(arr2)
    s_arr1 = sum(arr1)
    s_arr2 = sum(arr2)
    
    if l_arr1 == l_arr2:
        if s_arr1 < s_arr2:
            return -1
        elif s_arr1 > s_arr2:
            return 1
        else:
            return 0
        
    else:
        if l_arr1 < l_arr2:
            return -1
        elif l_arr1 > l_arr2:
            return 1
        else:
            return 0
        
        
        
    return answer