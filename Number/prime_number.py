# 소수 판별 알고리즘 - 에라토스테네스의 체

# 일반적인 소수 판별 알고리즘
# 예제 1 -  - 소규모 판별에만 적합
# 2 ~ N번째까지 모두 탐색하기 때문에 시간 복잡도는 O(n)
import math


def isPrimeNumber(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

# print(isPrimeNumber(97))


# 예제 2 - 제곱근을 이용한 알고리즘
# 시간 복잡도 O(n^(1/2))
def isPrimeNumber(x):
    end = int(math.sqrt(x))
    for i in range(2, end):
        if x % i == 0:
            return False
    return True


# 에라토스테네스의 체
number = 100000
a = [0] * number


def primeNumberSieve():
    for i in range(2, number):
        a[i] = i  # 모든 index에 값을 넣어줌
    for i in range(2, number):
        if a[i] == 0:  # 특정한 숫자들의 배수들을 지워주기
            continue  # 이미 지워진 숫자는 무시
        for j in range(i+i, number, i):  # 그 배수부터 출발해서 가능한 모든 숫자들을 지우기
            a[j] = 0
    for i in range(2, number):
        if a[i] != 0:  # index의 값이 0이 아닌 즉, 남은 소수들을 출력
            print(a[i])


primeNumberSieve()
