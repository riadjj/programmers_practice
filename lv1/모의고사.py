# --------------------------------------------------------
# https://programmers.co.kr/learn/courses/30/lessons/42840
# by riadjj@gmail.com
# --------------------------------------------------------

answers = [1,3,3,4,5]
# [1]

# answers = [1,3,2,4,2]
# [1,2,3]
# answers = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

result = []
p1 = [1, 2, 3, 4, 5] #* 8
p2 = [2, 1, 2, 3, 2, 4, 2, 5] #* 5
p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] #* 4
cnt = [0, 0, 0]

for i in range(len(answers)) : 
    if answers[i] == p1[i%5] : 
        cnt[0] += 1
    if answers[i] == p2[i%8] : 
        cnt[1] += 1
    if answers[i] == p3[i%10] : 
        cnt[2] += 1
print(cnt)

for i in range(len(cnt)) :
    if cnt[i] == max(cnt) :
        result.append(i+1)
        
print(result)
