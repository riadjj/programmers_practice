# --------------------------------------------------------
# https://programmers.co.kr/learn/courses/30/lessons/42889
# by riadjj@gmail.com
# --------------------------------------------------------

# https://programmers.co.kr/learn/courses/30/lessons/42889/solution_groups?language=python3&type=all 풀이 좀더 복습

N = 5
stages = [2,1,2,4,2,4,3,3]

result = {}
denominator= len(stages)                #stage의 개수 정의
for stage in range(1,N+1):              #stage 범위 반복문
    if denominator!=0:                  #denominator가 0이 아닌경우
        count = stages.count(stage)     #stage에 들어오는 숫자와 같은 숫자의 개수를 센다
        result[stage]=count/denominator
        denominator-=count
    else:
        result[stage]=0
    print(result)
print( sorted(result,key=lambda x: result[x],reverse=True) )

# {1: 0.125}
# {1: 0.125, 2: 0.42857142857142855}
# {1: 0.125, 2: 0.42857142857142855, 3: 0.5}
# {1: 0.125, 2: 0.42857142857142855, 3: 0.5, 4: 1.0}
# {1: 0.125, 2: 0.42857142857142855, 3: 0.5, 4: 1.0, 5: 0}
# [4, 3, 2, 1, 5]




# 마이
answer = []
fail_late = []
users = len(stages)

for i in range(1, N+1) : 
    count = stages.count(i)
    if users>0: fail = count/users
    else :      fail = 0
    fail_late.append(fail)
    users = users - count

max_num, max_ck = -1, -1
while 1 :
    for j in range(len(fail_late)) : 
        if fail_late[j] > max_num :
            max_num = fail_late[j]
            max_ck = j

    if max_ck == -1:
        break
    else :
        fail_late[max_ck] = -1
        answer.append(max_ck+1)
        max_num, max_ck = -1, -1

print('------')
print(answer)