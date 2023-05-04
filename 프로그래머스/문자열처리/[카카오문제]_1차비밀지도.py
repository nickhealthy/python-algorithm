# 1차 풀이
# 각각의 숫자를 이진수로 변환
# n의 자릿수로 맞춰주기
# 각 자릿수를 or 연산으로 더해주기
# 각 자릿수를 # 또는 공백으로 표시    
def solution(n, arr1, arr2):
    answer = []
    
    a1, a2 = [], []
    for i in arr1:
        pwd = bin(i)[2:]
        tmp = len(pwd)
        if tmp < n:
            a1.append(('0' * (n - tmp)) + pwd)
        else:
            a1.append(pwd)

    for i in arr2:
        pwd = bin(i)[2:]
        tmp = len(pwd)
        if tmp < n:
            a2.append(('0' * (n - tmp)) + pwd)
        else:
            a2.append(pwd)

    for i in range(n):
        tmp = ''
        for j in range(n):
            if a1[i][j] == '1' or a2[i][j] == '1':
                tmp += '1'
            else:
                tmp += '0'
        answer.append(tmp)

    result = []
    for i in range(n):
        tmp = ''
        for j in range(n):
            if answer[i][j] == '1':
                tmp += '#'
            else:
                tmp += ' '
        
        result.append(tmp)
        
    return result

# 다른 사람 풀이
def solution(n, arr1, arr2):
    answer = []
    for a1, a2 in zip(arr1, arr2):
        a12 = bin(a1 | a2)[2:]
        a12 = a12.rjust(n, '0')
        a12 = a12.replace('1', '#')
        a12 = a12.replace('0', ' ')
        answer.append(a12)

    return answer