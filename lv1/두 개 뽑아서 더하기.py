# --------------------------------------------------------
# https://programmers.co.kr/learn/courses/30/lessons/68644
# by riadjj@gmail.com
# --------------------------------------------------------

numbers = list(map(int, input().split()))
answer = list()

for i in range(0, len(numbers)-1) : 
    for j in range(i+1, len(numbers)) : 
        answer.append(numbers[i] + numbers[j])

set = set(answer)
answer = list(set)
answer.sort()
print(answer)