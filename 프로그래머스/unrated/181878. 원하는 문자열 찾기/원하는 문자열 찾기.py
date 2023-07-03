def solution(myString, pat):
    myString = myString.lower()
    pat = pat.lower()
    
    if myString.find(pat) == -1:
        return 0
    else:
        return 1
        
    
    return answer