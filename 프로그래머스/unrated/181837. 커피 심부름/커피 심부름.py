def solution(order):
    dic = {'americano': 4500, 'cafelatte': 5000, 'anything': 4500}
    
    answer = 0
    for i in order:
        if 'anything' == i:
            answer += 4500
        elif 'americano' in i:
            answer += 4500
        else:
            answer += 5000
            
    return answer
            