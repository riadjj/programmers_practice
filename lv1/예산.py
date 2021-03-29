# --------------------------------------------------------
# https://programmers.co.kr/learn/courses/30/lessons/12982
# by riadjj@gmail.com
# --------------------------------------------------------

d = [1,3,2,5,4]
budget = 9
answer = 0

# my
d.sort()
# for i in d : # 이렇게 써야되는데 계속 길이로 생각하게 되네 :<
for i in range(len(d)) : 
    budget -= d[i]
    if (budget >= 0) : 
        answer += 1
    else :
        break
print(answer)