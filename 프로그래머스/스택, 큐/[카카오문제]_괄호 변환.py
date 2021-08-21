def parse(less):
    corret = True
    left = 0
    right = 0
    stack = []

    for i in range(len(less)):
        if less[i] == '(':
            left += 1
            stack.append('(')
        else:
            # 올바른 문자열 검증. 즉, '('로 시작 안할 시, 거짓
            if len(stack) == 0:
                right += 1
                corret = False
            else:
                right += 1
                stack.pop()
        
        if left == right:
            return i + 1, corret

    return 0, False

def solution(p):
    if len(p) == 0:
        return p

    # 올바른 문자열, 균형잡힌 문자열 최소 u를 구하기 위한 함수
    pos, correct = parse(p)
    u = p[:pos]
    v = p[pos:]

    # 올바른 괄호 문자열이라면
    if correct:
        return u + solution(v)

    answer = '(' + solution(v) + ')'
    
    for i in range(1, len(u) - 1):
        if u[i] == '(':
            answer += ')'
        else:
            answer += '('

    return answer

p = "()))((()"
print(solution(p))