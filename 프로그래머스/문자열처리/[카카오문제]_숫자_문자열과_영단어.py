word = ("zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine")

def solution(s):
    result = ''
    
    pos = 0
    while pos < len(s):
        if s[pos] >= '0' and s[pos] <= '9':
            result += s[pos]
            pos += 1
        else:
            for i in range(len(word)):
                # word 튜플에서 맞는 값을 찾았다면
                if s.find(word[i], pos, pos + 5) != -1:
                    result += str(i)
                    pos += len(word[i])
                    break
    
    return int(result)