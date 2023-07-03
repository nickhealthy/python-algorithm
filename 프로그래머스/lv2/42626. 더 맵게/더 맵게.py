# import heapq

# def solution(scoville, K):
#     answer = 0
#     heapq.heapify(scoville)

#     while scoville[0] < K:
#         mix = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
#         heapq.heappush(scoville, mix)
#         answer += 1
#         if len(scoville) == 1 and scoville[0] < K:
#             return -1

#     return answer

# 2023.06.25 재풀이
from heapq import heappop, heappush, heapify

def solution(scoville, K):
    answer = 0
    
    heapify(scoville)
    while True:
        min1 = heappop(scoville)
        # 스코빌 지수를 K 이상으로 모두 만들거나, 만들 수 없는 경우
        if min1 >= K:
            break
        elif len(scoville) == 0:
            answer = -1
            break
            
        min2 = heappop(scoville)
        new_scoville = min1 + min2 * 2
        heappush(scoville, new_scoville)
        
        answer += 1
    
    return answer