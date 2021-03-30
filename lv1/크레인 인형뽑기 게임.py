# --------------------------------------------------------
# https://programmers.co.kr/learn/courses/30/lessons/64061
# by riadjj@gmail.com
# --------------------------------------------------------

def rotated(m):
    N = len(m) 
    ret = [[0] * N for _ in range(N)]
    for r in range(N): 
        for c in range(N): 
            # ret[c][N-1-r] = m[r][c] # 90
            # ret[N-1-r][N-1-c] = m[r][c] # 180
            ret[N-1-c][r] = m[r][c] # 270
    return ret

# board = [[0,0,0,0,0],
#         [0,0,1,0,3],
#         [0,2,5,0,1],
#         [4,2,4,4,2],
#         [3,5,1,3,1]]
# moves = [1,5,3,5,1,2,1,4]
# # 4 터트려져 사라진 인형의 개수

board = [[0, 0, 0, 0, 0],
        [0, 0, 1, 0, 3],
        [0, 2, 5, 0, 1],
        [4, 2, 4, 4, 2],
        [3, 5, 1, 3, 1]]
# moves = [1, 5, 3, 5, 1, 2, 5, 1, 4, 3]


# board = [[0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 3, 0], [0, 2, 5, 0, 1, 0], [4, 2, 4, 4, 2, 0], [3, 5, 1, 3, 1, 0], [3, 5, 1, 3, 1, 1]]
# moves = [1, 5, 3, 5, 1, 2, 5, 1, 4, 3, 1, 2, 6, 6, 6]
# 8

# board = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
board = [[1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
moves = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

# my
answer = 0
pick = []
board = rotated(board)
lenth = len(board)
# print(base_lenth)
# 1 -> 4
# 5 -> 0
# 5-move

print('-----Board ----')
for b in board : 
    print(b)
print('---------------')

for move in moves : 
    for i in range(len(board[lenth-move])) :

        if board[lenth-move][i] != 0 :
            print('select', move, 'pcik:', board[lenth-move][i])
            pick.append(board[lenth-move][i])
            board[lenth-move][i] = 0

            if len(pick) == len(board) :
                de = pick[-1]
                while pick.count(de) != 0:
                    pick.remove(de)
                    answer += 1
            else :
                for j in range(len(pick)-1):
                    if pick[j] == pick[j+1] :
                        pick.pop()
                        pick.pop()
                        answer += 2
            print(pick, ' ans:', answer)
            break
    print('-----Board ----')
    for b in board : 
        print(b)
    print('---------------')

# 터지는 조건이 2개 구나
# 연속
# 5번 위치에 있을 때 

# print('----')
# print(pick)
print(answer)
