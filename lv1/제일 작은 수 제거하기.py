# --------------------------------------------------------
# https://programmers.co.kr/learn/courses/30/lessons/12935
# by riadjj@gmail.com
# --------------------------------------------------------

arr = [4, 3, 2, 1]
answer = [] # [4, 3, 2]

# my
arr.remove(min(arr))
if len(arr) == 0 :
    arr.append(-1)
print(arr)

# more+
if len(arr) <= 1 :
    print([-1])
else :
    arr.remove(min(arr))
    print(arr)