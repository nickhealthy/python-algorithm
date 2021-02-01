array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

# 다른 사람 코드
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

# 통과
def solution(array, commands):
    ans = []
    answer = []
    for i in range(len(commands)):
        ans = array[commands[i][0]-1 : commands[i][1]]
        ans.sort()
        answer.append(ans[commands[i][-1]-1])
    return answer
 


# 두번째 방안
'''
ans = []
answer = []
# 0, 1, 2
for i in range(len(commands)):
    ans = array[commands[i][i]-1 : commands[i][i+1]]
    ans.sort()
    answer.append(ans[commands[i][2]-1])
print(answer)


#array = array[commands[0][0]-1:commands[0][1]]
#array.sort()
#print(array)
'''


# 첫번째 방안
'''
temp = []
ans = []
ans2 = []
for i in range(len(commands)):
    for j in range(len(commands)-1):
        temp = array
        ans = temp[commands[i][j]-1:commands[i][j+1]]
        ans.sort()
        # 2,3,5,6
        ans2.append(ans[commands[i][2]-1])
        temp = []
'''
