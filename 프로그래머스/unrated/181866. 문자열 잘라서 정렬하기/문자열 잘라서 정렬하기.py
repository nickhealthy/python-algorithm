def solution(myString):
    answer = myString.split('x')
    answer = ' '.join(answer).split()
    return sorted(answer)