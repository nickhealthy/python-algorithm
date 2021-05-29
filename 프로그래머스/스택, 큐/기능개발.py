# zip으로 각 프로세스와, 스피드를 더한다.
# 날짜 계산을 따로해서 앞의 인덱스가 뒤의 인덱스보다 
# 숫자가 이상이라면 작은것들을 모두 묶어서 cnt += 1을 해준다.

# solution 1
# def solution(progresses, speeds):
#     answer = []
#     tmp = []
#     for progress, speed in zip(progresses, speeds):
#         cnt = 0
#         while True:
#             if progress >= 100:
#                 tmp.append(cnt)
#                 break
#             else:
#                 progress += speed
#                 cnt += 1

#     front = 0
#     for idx in range(len(tmp)):
#         if tmp[idx] > tmp[front]:
#             answer.append(idx - front)
#             front = idx 
#     answer.append(len(tmp) - front)

#     return answer
        
# solution 2

def solution(progresses, speeds):
    time = 0
    count = 0
    answer = []
    while len(progresses) > 0:
        # 기능개발을 맞춘거라면
        if progresses[0] + speeds[0] * time >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            # 카운트가 하나라도 올라가있으면 기능개발이 완료되었으므로
            # 카운트가 2이상이라면 배포가 한번에 2개가 되는 것
            if count > 0:
                answer.append(count)
                count = 0
        # 시간은 일정하게 1씩(하루)증가
        time += 1
    answer.append(count)
    return answer
    