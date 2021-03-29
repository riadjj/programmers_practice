# --------------------------------------------------------
# https://programmers.co.kr/learn/courses/30/lessons/42748
# by riadjj@gmail.com
# --------------------------------------------------------

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
answer = [] # [5, 6, 3]

# my
for i in range(len(commands)) : 
    tmp = array[commands[i][0]-1:commands[i][1]]       
    tmp.sort()
    answer.append(tmp[commands[i][2]-1])

print(answer)

# other
for i,j,k in commands:
    answer.append(sorted(array[i-1:j])[k-1])
    
print(answer)