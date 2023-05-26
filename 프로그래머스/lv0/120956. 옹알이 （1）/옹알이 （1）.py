def solution(babbling):
    result = 0
    
    for i in babbling:
        word = ''
        answer = 0
        
        for j in i:
            word += j
            if word in ["aya", "ye", "woo", "ma"]:
                word = ''
                answer += 1
                
        if not len(word) and answer > 0:
            result += 1
            
    
    return result