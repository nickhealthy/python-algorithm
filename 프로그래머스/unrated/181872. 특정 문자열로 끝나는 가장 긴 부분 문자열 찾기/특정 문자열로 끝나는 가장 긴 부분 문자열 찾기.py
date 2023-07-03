def solution(myString, pat):
    answer = ''
    for i in range(len(myString)):
        if myString[i:len(pat) + i] == pat:
            answer = myString[:i + len(pat)]
    return answer
