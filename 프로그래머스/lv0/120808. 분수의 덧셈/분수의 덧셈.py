def solution(numer1, denom1, numer2, denom2):
    # 1. 두 분수의 합 구하기
    boonja = numer1 * denom2 + numer2 * denom1
    boonmo = denom1 * denom2

    # 2. 분수의 최대 공약수 구하기
    start = max(boonja, boonmo)
    gcd_value = 1
    for num in range(start, 0, -1):
        if boonja % num == 0 and boonmo % num == 0:
            gcd_value = num
            break

    # 3. 기약분수 구하기
    return [boonja / gcd_value, boonmo / gcd_value]