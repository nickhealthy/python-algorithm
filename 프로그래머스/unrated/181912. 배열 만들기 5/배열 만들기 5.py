def solution(intStrs, k, s, l):
    answer = []
    
    for intS in intStrs:
        convS = int(intS[s: s + l])
        if convS > k:
            answer.append(convS)
    
    return answer