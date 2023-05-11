def solution(my_string, m, c):
    answer = ''

    length = len(my_string)
    for i in range(length):
        if (c + m * i) > length:
            break
        
        answer += my_string[c + m * i - 1]

    return answer