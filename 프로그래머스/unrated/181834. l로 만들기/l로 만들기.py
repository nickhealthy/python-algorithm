# def solution(myString):
#     answer = ''
#     for i in myString:
#         print(i)
#         if i < "l":
#             answer += 'l'
#             continue
#         answer += i
#     return answer

def solution(myString):
    return myString.translate(str.maketrans('abcdefghijk', 'lllllllllll'))