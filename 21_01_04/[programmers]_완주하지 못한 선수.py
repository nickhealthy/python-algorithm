participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

participant.sort()
completion.sort()

# 첫번째 풀이
# def solution(participant, completion):    
#     for i in range(len(participant)):
#         if participant[i] not in completion:
#             return participant[i]

# 성공
def solution(participant, completion):
    for i, z in zip(participant, completion):
        print(i, z)
        if i != z:
            return i
    return participant[-1]


# 참고
from collections import Counter

def solution(participant, completion):
    ans = Counter(participant) - Counter(completion)
    return list(ans)[0]

print(solution(participant, completion))
