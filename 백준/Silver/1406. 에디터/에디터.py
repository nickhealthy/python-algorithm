import sys

input = sys.stdin.readline

lstA = list(input().rstrip())
lstB = []
for _ in range(int(input())):
    command = input().split()
    
    if command[0] == 'L':
        if lstA:
            lstB.append(lstA.pop())
    
    elif command[0] == 'D':
        if lstB:
            lstA.append(lstB.pop())
    
    elif command[0] == 'B':
        if lstA:
            lstA.pop()
    
    else:
        lstA.append(command[1])
    
lstA.extend(reversed(lstB))
print(''.join(lstA))
