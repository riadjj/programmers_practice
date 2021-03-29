# --------------------------------------------------------
# https://programmers.co.kr/learn/courses/30/lessons/12950
# by riadjj@gmail.com
# --------------------------------------------------------

arr1 = [[1,2],[2,3]]
arr2 = [[3,4],[5,6]]
# [[4,6],[7,9]]

# arr1 = [[1],[2]]
# arr2 = [[3],[4]]
# [[4],[6]]

# my
answer = []
for i in range(len(arr1)) : 
    sum = []
    for j in range(len(arr1[i])) : 
        sum.append( arr1[i][j]+arr2[i][j] )
    answer.append(sum)
print(answer)

# other 1
answer = [[c + d for c, d in zip(a, b)] for a, b in zip(arr1,arr2)]
print(answer)

# other 2
n, m = len(arr1), len(arr1[0])
answer = [[arr1[i][j] + arr2[i][j] for j in range(m)] for i in range(n)]
print(answer)

