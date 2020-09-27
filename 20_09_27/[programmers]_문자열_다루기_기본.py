s = "a234"
s1 = "12342"

def solution(s):
    if len(s) == 4 or len(s) == 6:
        s = sorted(s)
        test = 0
        for i in s:
            if ((47 < ord(i)) & (58 > ord(i))):
                pass
            else:
                test += 1

        if test >= 1:
            return False
        else:
            return True
    
    else:
        return False
    