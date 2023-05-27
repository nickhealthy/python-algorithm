# def solution(babbling):
#     result = 0
    
#     for i in babbling:
#         word = ''
#         answer = 0
        
#         for j in i:
#             word += j
#             if word in ["aya", "ye", "woo", "ma"]:
#                 print(word)
#                 word = ''
#                 answer += 1
                
#         if not len(word) and answer > 0:
#             result += 1
            
    
#     return result


# 2번 풀이
# def solution(babbling):
#     c = 0
#     for b in babbling:
#         for w in [ "aya", "ye", "woo", "ma" ]:
#             if w * 2 not in b:
#                 b = b.replace(w, ' ')
#         if len(b.strip()) == 0:
#             c += 1
#     return c


# 3번 풀이
import re

def solution(babbling):
    regex = re.compile('^(aya|ye|woo|ma)+$')
    
    cnt = 0
    for e in babbling:
        if regex.match(e):
            cnt += 1
    
    return cnt