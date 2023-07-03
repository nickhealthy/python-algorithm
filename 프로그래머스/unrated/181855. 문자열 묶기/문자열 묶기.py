from collections import defaultdict

def solution(strArr):
    answer = 0
    dic = defaultdict(int)
    
    for i in strArr:
        dic[len(i)] += 1
        
    return max(dic.values())