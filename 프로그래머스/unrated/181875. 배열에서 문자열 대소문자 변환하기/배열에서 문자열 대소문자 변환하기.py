def solution(strArr):
    for idx, val in enumerate(strArr):
        if idx % 2 == 0:
            strArr[idx] = val.lower()
        else:
            strArr[idx] = val.upper()
            
    
    return strArr