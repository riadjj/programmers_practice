# --------------------------------------------------------
# https://programmers.co.kr/learn/courses/30/lessons/49994
# by riadjj@gmail.com
# --------------------------------------------------------

dir = 'ULURRDLLU'
# 7
answer = 0

# 0, 0
# U D R L 
# 한칸씩 이동하는데
# 걸어간 길이 구하는 문제
# 단 중복된 길이는 뺀다
# 이거 패스 문젠데?
# 스택? 셋? 
path = set()
nowPos = [0, 0]

for i in range(len(dir)) : 
    nextPos = [0, 0]
    if dir[i] == 'U' :
        nextPos = [nowPos[0], nowPos[1]+1]
    elif dir[i] == 'D' :
        nextPos = [nowPos[0], nowPos[1]-1]
    elif dir[i] == 'R' :
        nextPos = [nowPos[0]+1, nowPos[1]]
    elif dir[i] == 'L' :
        nextPos = [nowPos[0]-1, nowPos[1]]
    
    if -5 <= nextPos[0] <= 5 and -5 <=nextPos[1] <= 5 :
        path.add((nowPos[0], nowPos[1], nextPos[0], nextPos[1]))
        path.add((nextPos[0], nextPos[1], nowPos[0], nowPos[1]))
        nowPos = nextPos
    
# print(path)

print(len(path)//2)





# print(answer)
