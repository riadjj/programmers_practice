# --------------------------------------------------------
# https://programmers.co.kr/learn/courses/30/lessons/42861
# by riadjj@gmail.com
# --------------------------------------------------------

graph = [[0,1,1], #0과 1 연결 할때 1든다
        [0,2,2],
        [1,2,5],
        [1,3,1],
        [2,3,8]]
n = 4
answer = 0

graph.sort(key = lambda x:x[2])
mst=[]
p=[i for i in range(n+1)]

def find(u):
    if u != p[u]:
        p[u] = find(p[u])
    return p[u]

while len(mst) != n-1:
    u, v, wt = graph.pop(0)
    if find(u) != find(v):
        p[find(u)] = find(v)
        mst.append((u, v)) 
        answer += wt

# print('최소신장트리: ',mst)
# print('최소신장트리 가중치:', answer)
print(answer)
