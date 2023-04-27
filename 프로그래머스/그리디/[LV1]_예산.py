# 그리디 문제
def solution(d, budget):
    answer = 0

    # 가장 많은 수의 부서를 지원해줘야 하므로 각 부서에서 요청한 작은 금액부터 처리해주고 count를 센다.
    for i in sorted(d):
        if budget - i >= 0:
            budget -= i
            answer += 1

    return answer


print(solution([2,2,3,3], 10))
