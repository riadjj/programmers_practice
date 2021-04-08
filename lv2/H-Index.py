# --------------------------------------------------------
# https://programmers.co.kr/learn/courses/30/lessons/
# by riadjj@gmail.com
# --------------------------------------------------------

citations = [10, 9, 4, 1, 1]
# [3, 0, 6, 1, 5]

# [12, 11, 10, 9, 8, 1] 5
# [6, 6, 6, 6, 6, 1] 5
# [4, 4, 4] 3
# [4, 4, 4, 5, 0, 1, 2, 3] 4
# [10, 11, 12, 13] 4
# [3, 0, 6, 1, 5] 3
# [0, 0, 1, 1] 1
# [0, 1] 1
# [10, 9, 4, 1, 1] 3
answer = 0

# my
citations.sort(reverse=True)

if citations[0] == 0:
    answer = False

for i in range(len(citations)) : 
    if citations[i] > i :
        answer += 1
    else :
        break

print(answer)


# other shocking...
answer = max(map(min, enumerate(citations, start=1)))
