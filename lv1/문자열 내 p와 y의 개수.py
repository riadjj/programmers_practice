# --------------------------------------------------------
# https://programmers.co.kr/learn/courses/30/lessons/12916
# by riadjj@gmail.com
# --------------------------------------------------------

s = 'pPoooyY'
# p y 숫자비교
np,ny = 0, 0
for i in range(len(s)) : 
    if s[i] == 'p' or s[i] == 'P' : np += 1
    elif s[i] == 'y' or s[i] == 'Y' : ny += 1
print( True if np==ny else False )

# count 사용
print(s.lower().count('p') == s.lower().count('y'))

# Counter 사용
from collections import Counter
c = Counter(s.lower())
print(c['y'] == c['p'])