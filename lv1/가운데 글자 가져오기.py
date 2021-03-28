# --------------------------------------------------------
# https://programmers.co.kr/learn/courses/30/lessons/12903
# by riadjj@gmail.com
# --------------------------------------------------------

s = "qwer"
ans = ''
l = len(s)
if l%2 == 0 : 
    ans = ans + s[int(l/2)-1]
    ans = ans + s[int(l/2)]
else :
    ans = ans + s[int(l/2)]

print(ans)