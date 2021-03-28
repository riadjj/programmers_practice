# --------------------------------------------------------
# https://programmers.co.kr/learn/courses/30/lessons/12918
# by riadjj@gmail.com
# --------------------------------------------------------

s = '1234'

print( (len(s) == 4 or len(s) ==6) and s.isdigit() )

if len(s) >= 4 and len(s) <= 6 :
    print(s.isdigit())
else:
    print('False')