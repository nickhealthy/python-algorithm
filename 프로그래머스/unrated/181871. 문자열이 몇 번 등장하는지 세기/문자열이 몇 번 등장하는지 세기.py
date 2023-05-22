def solution(myString, pat):
    answer = 0
    length = len(pat)
    for i in range(len(myString)):
        if myString[i:length + i] == pat:
            answer += 1
    return answer