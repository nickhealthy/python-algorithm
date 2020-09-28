def no_continuous(s):
    a=[ v for i,v in enumerate(s) if s[i-1] != s[i] or i == 0]

    return a

'''
arr = [1,1,3,3,0,1,1]
print(no_continuous(arr))
'''