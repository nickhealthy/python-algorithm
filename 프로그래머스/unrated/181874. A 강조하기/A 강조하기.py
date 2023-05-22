def solution(myString):
    answer = ''
    for spell in myString:
        if spell == 'a' or spell == 'A':
            answer += spell.upper()
        else:
            answer += spell.lower()
    return answer