import sys
input = sys.stdin.readline

TC = int(input())

for i in range(TC):
    process_list = list(input().rstrip())
    n = int(input().rstrip())
    nums = input()[1:-2].rstrip().split(',')

    reverse_count = 0 # 홀/짝 뒤집힌 횟수용
    del_front = 0 # 앞에서 빠질 수(슬라이싱)
    error = False

    for process in process_list:
        if process == "R":
            reverse_count += 1
        else:
            try:
                if reverse_count % 2 == 1:
                    nums.pop()
                else:
                    del_front += 1
            except:
                error = True
                break
    
    # 에러처리
    if error or n < del_front:
        print("error")
        continue

    # reverse_count 홀/짝 여부에 따라 순선 변경
    if reverse_count % 2 == 0:
        nums = nums[del_front:]
    else:
        nums = list(reversed(nums[del_front:]))

    # 출력
    print('[', end='')
    for i in range(len(nums)):
        if i == len(nums) - 1:
            print(nums[i], end='')
        else:
            print(f'{int(nums[i])},', end='')
    print(']')