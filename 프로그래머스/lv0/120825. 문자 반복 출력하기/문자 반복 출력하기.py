def solution(my_string, n):
    answer = ''
    for word in my_string:
        answer += word * n
        
    return answer