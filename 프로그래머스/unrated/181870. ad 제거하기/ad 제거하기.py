def solution(strArr):
    answer = []
    for word in strArr:
        if word.find("ad") == -1:
            answer.append(word)
    return answer