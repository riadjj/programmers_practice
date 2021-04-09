# --------------------------------------------------------
# https://programmers.co.kr/learn/courses/30/lessons/42586
# by riadjj@gmail.com
# --------------------------------------------------------

import math
from collections import deque

# progresses = [93, 30, 55]
# speeds = [1, 30, 5]

progresses = [95, 90, 99, 99, 80, 99]	
speeds = [1, 1, 1, 1, 1, 1]

answer = []

result = deque()

for i in range(len(progresses)) : 
    result.append( math.ceil((100 - progresses[i])/speeds[i]) )

# 큐로 뽑자~!
n, count = -1, 0
while 1 :
    if n == -1:
        n = result.popleft()
        count += 1

    if len(result) == 0 :
        answer.append(count)
        break
    elif n < result[0] :
        answer.append(count)
        n = -1
        count = 0
    else :
        result.popleft()
        count += 1

print(answer)

