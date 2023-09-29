def solution(s):
    answer = ''
    STRING_LENGTH = len(s)
    
    if STRING_LENGTH % 2 == 0:
        answer = s[(STRING_LENGTH - 1) // 2 : (STRING_LENGTH) // 2 + 1]
    else:
        answer = s[STRING_LENGTH // 2]
    return answer