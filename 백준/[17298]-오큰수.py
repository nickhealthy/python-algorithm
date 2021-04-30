n = int(input())
nums = list(map(int, input().split()))

stack = []
result = [-1 for _ in range(n)] # 오큰수를 찾지 못했을 때 -1 값 출력

i = 0
stack.append(0)

# 스택에 값이 있을 때 and i < n번까지
while stack and i < n:
    # 스택에 값이 있을 때 and 스택의 마지막 인덱스보다 nums[i]값이 크다면 == 오큰수
    while stack and nums[stack[-1]] < nums[i]:
        result[stack[-1]] = nums[i] # 오큰수 인덱스 자리에 맞게 삽입
        stack.pop()

    stack.append(i)
    i += 1


for i in result:
    print(i, end=' ')