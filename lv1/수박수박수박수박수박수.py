# --------------------------------------------------------
# https://programmers.co.kr/learn/courses/30/lessons/12922
# by riadjj@gmail.com
# --------------------------------------------------------

n = int(input())
answer = ''
for i in range(n) : 
    if i%2==0:  answer += '수'
    else :  answer += '박'
print(answer)