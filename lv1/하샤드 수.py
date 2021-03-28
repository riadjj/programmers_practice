# --------------------------------------------------------
# https://programmers.co.kr/learn/courses/30/lessons/12947
# by riadjj@gmail.com
# --------------------------------------------------------

x = int(input())

tmp = x
dx = 0
while 1:
    dx += tmp%10 
    tmp = int(tmp/10)
    if tmp == 0:
        break;
if x%dx == 0 : print('true')
else : print('false')

if x % sum([int(c) for c in str(x)]) == 0 : print('true')
else : print('false')
