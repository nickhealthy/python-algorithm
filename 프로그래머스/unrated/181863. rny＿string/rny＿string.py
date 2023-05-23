def solution(rny_string):
    answer = ''
    
    for string in rny_string:
        if string == 'm':
            answer += 'rn'
            continue
        
        answer += string
    
    return answer