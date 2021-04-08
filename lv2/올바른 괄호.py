# --------------------------------------------------------
# https://programmers.co.kr/learn/courses/30/lessons/12909
# by riadjj@gmail.com
# --------------------------------------------------------

# s = "(())()"
s = "()))((()"	
answer = True

x1, x2 = 0, 0

if s[0] == ')' or s[len(s)-1] == '(':
    answer = False

for c in s :
    if c == '(':
        x1 += 1
    elif c == ')':
        x2 += 1
    if x2 > x1 :
        answer = False
        break

if x1 == x2 :
    answer = True
else :
    answer = False

print(answer)

