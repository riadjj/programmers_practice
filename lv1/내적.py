# --------------------------------------------------------
# https://programmers.co.kr/learn/courses/30/lessons/70128
# by riadjj@gmail.com
# --------------------------------------------------------

a = [1,2,3,4]
b = [-3,-1,0,2]
# 3

# a = [-1,0,1]
# b = [1,0,-1]
# -2

# my
answer = 0
for i in range(len(a)) : 
    answer += a[i] * b[i]
print(answer)

# other 1
print(sum([x*y for x, y in zip(a,b)]))

# other 2
answer = 0
for x, y in zip(a,b):
    answer += x*y
print(answer)