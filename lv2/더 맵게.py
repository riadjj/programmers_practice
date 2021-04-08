# --------------------------------------------------------
# https://programmers.co.kr/learn/courses/30/lessons/
# by riadjj@gmail.com
# --------------------------------------------------------

import heapq

scoville = [1, 2, 3]
K = 11

answer = 0

heapq.heapify(scoville)
print(scoville)

mix_cnt = 0
while scoville[0] < K:
    try:
        heapq.heappush(scoville, heapq.heappop(scoville) + (heapq.heappop(scoville) * 2))
        print(scoville)
    except IndexError:
        print(-1)
    mix_cnt += 1
print(mix_cnt)
