# from collections import Counter
# Counter 메서드는 각각의 값들이 몇 개가 있는지 dict() 형태의 타입으로 만들어 줌


# 예시
participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

from collections import Counter

def solution(participant, completion):
    ans = Counter(participant) - Counter(completion)
    return list(ans)[0]

print(solution(participant, completion))


# 결과
# mislav