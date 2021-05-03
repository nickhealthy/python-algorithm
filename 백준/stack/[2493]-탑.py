# # 내 풀이

# import sys

# input = sys.stdin.readline
# n = int(input().rstrip())
# top_list = list(map(int, input().rstrip().split()))

# stack = []

# for i in range(len(top_list)-1, -1, -1): # 4
    
#     while n != 0:
#         n -= 1
#         if top_list[i] < top_list[n]:
#             stack.append(n+1)
#             break
#     else:
#         stack.append(0)
        
#     n = i

# for _ in range(len(stack)):
#     print(stack.pop(), end=' ')


# 다른 사람 풀이

n = int(input())
top_list = list(map(int, input().split()))

stack = [] # 최대값을 저장할 스택
answer = [] # 수신 탑 인덱스 저장

for i in range(n):
    while stack:
        if stack[-1][1] > top_list[i]: # 수신 가능한 상황
            answer.append(stack[-1][0] + 1)
            break
        else: # 현재 인덱스가 이전 인덱스보다 크다면 이전 인덱스 pop(최대값을 갱신)
            stack.pop()
    # 수신할 탑이 없다면 0 삽입
    if not stack:
        answer.append(0)

    stack.append((i, top_list[i])) # 값, 인덱스

print(*answer)