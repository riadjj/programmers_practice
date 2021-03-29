# --------------------------------------------------------
# https://programmers.co.kr/learn/courses/30/lessons/12930
# by riadjj@gmail.com
# --------------------------------------------------------

s = 'try hello world'
answer = ''
# TrY HeLlO WoRlD
idx=0
for i in range(len(s)) : 
    if s[i] == ' ':
        answer += ' '
        idx = 0
        continue
    elif (idx%2 == 0) : 
        answer += s[i].upper()
    else :
        answer += s[i].lower()
    idx += 1    
    
print(answer)
