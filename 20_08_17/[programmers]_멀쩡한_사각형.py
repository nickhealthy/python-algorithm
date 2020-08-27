import math

def solution(w,h):
    # 반복되는 최소 부분에서 지나는 사각형의 수 구하는 함수
    def find_sqr(w,h):
        # 한 변이라도 1이라면 모든 사각형 다 지난다
        if w == 1 or h ==1 :
            return w * h
        else :            
            min = int(w if w < h else h)
            max = int(w if w > h else h)
            # 답 넣을 변수
            num = 0
            # start 변수
            start = 1
            # 더 작은 숫자로 for문 돌리기
            for x in range(1,min+1):
                end = math.ceil(max/min)*x
                # ceil로 하면 마지막단계에서 max 값이 넘는다.
                if end > max :
                    end = max
                num += end -start +1
                start = end
            return num  
    # 전체 칸
    answer = w * h
    # w,h의 최대공약수(반복횟수) 구하기
    max_div = math.gcd(w,h)
    # 최소부분의 지나는 사각형의 개수 * 반복횟수
    del_num = max_div * find_sqr(w/max_div, h/max_div)
    # 답 구하기
    answer -= del_num
    return answer