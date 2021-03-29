# --------------------------------------------------------
# https://programmers.co.kr/learn/courses/30/lessons/67256
# by riadjj@gmail.com
# --------------------------------------------------------

def pathLen(nowPos, goalPos) :
    return abs(nowPos[0]-goalPos[0])+abs(nowPos[1]-goalPos[1])

# numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
# hand = 'right'
# LRLLLRLLRRL
# LRLLLRLLRRL

numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = 'left'
# LRLLRRLLLRR
# LRLLRRLLLRR

answer = ''

pos_left = { 1:[0, 3], 2:[1, 3],
            4:[0, 2], 5:[1, 2],
            7:[0, 1], 8:[1, 1],
            10:[0, 0], 0:[1, 0] }
pos_right = { 3:[0, 3], 2:[1, 3],
            6:[0, 2], 5:[1, 2],
            9:[0, 1], 8:[1, 1],
            12:[0, 0], 0:[1, 0] }
now_left = 10 #기준점 10
now_right = 12 #기준점 12

for i in numbers:
    # left
    # if i==1 or i==4 or i==7 or i==10 :
    if i in [1, 4, 7, 10]:
        now_left = i
        answer += 'L'
    # right
    # elif i==3 or i==6 or i==9 or i==12 :
    elif i in [3, 6, 9, 12]:
        now_right = i
        answer += 'R'
    # calc
    else :
        left = pathLen(pos_left[now_left], pos_left[i])
        right = pathLen(pos_right[now_right], pos_right[i])
        
        if left < right or (left == right and hand == 'left') :
            now_left = i
            answer += 'L'
        elif right < left or (left == right and hand == 'right') :
            now_right = i
            answer += 'R'

print(answer)
