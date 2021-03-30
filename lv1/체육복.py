# --------------------------------------------------------
# https://programmers.co.kr/learn/courses/30/lessons/
# by riadjj@gmail.com
# --------------------------------------------------------

answer = 0
n = 5
lost = [2, 4] 
reserve = [1, 3, 5]

n=5
lost=[2,4,5]
reserve=[1,4] #=> 4

# n=2
# lost=[1]
# reserve=[2] #=> 2

# n=5
# lost=[1,2,3]
# reserve=[2,3,4] #=> 4

# n=4
# lost=[3,1,2]
# reserve=[2,4,3] #=> 3

# n=3
# lost=[1,2]
# reserve=[2,3] #=> 2

# n=8
# lost=[1,3,5,7]
# reserve=[2,4,6,8]

# other
reser_del = set(reserve)-set(lost) 
lost_del = set(lost)-set(reserve)
for i in reser_del:
    if i-1 in lost_del:
        lost_del.remove(i-1) 
    elif i+1 in lost_del: 
        lost_del.remove(i+1)
answer = n-len(lost_del)
print(answer)

print('----------')

# my 
# 테스트 케이스 5 7 10 11 실패?
# 뭐가 문제인가 아하 분배조건 실수
total = [1 for i in range(n)]
for i in range(len(lost)) : 
   total[lost[i]-1] -= 1
for i in range(len(reserve)) : 
    total[reserve[i]-1] += 1
print(total)

for i in range(n) :
    if total[i] == 0 :
        if i<n-1:
            if total[i+1]>1:
                total[i+1] -= 1
                total[i] += 1
        if i>=1:
            if total[i-1]>1:
                total[i-1] -= 1
                total[i] += 1
print(total)
answer = sum([1 for i in total if i > 0])

print(answer)
