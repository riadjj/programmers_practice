# --------------------------------------------------------
# https://programmers.co.kr/learn/courses/30/lessons/12973
# by riadjj@gmail.com
# --------------------------------------------------------

s = 'baabaa' 
# 1
# abccccbaaa 1
# abccaabaa 0

answer = 0

stack = []

for c in s : 
    stack.append(c)

    if len(stack) >= 2 :
        if stack[-1] == stack[-2] :
            stack.pop()
            stack.pop()
        
if len(stack) > 0 :
    answer = 0
else :
    answer = 1

print(answer)

