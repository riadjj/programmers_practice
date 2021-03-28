# --------------------------------------------------------
# https://programmers.co.kr/learn/courses/30/lessons/12906
# by riadjj@gmail.com
# --------------------------------------------------------

arr = [1, 1, 3, 3, 0, 1, 1]
answer = []
answer.append(arr[0])
index = 0

for i in range(len(arr)):
    if answer[index] != arr[i] :
        answer.append(arr[i])
        index = index + 1

print(answer)