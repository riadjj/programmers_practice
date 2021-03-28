# --------------------------------------------------------
# https://programmers.co.kr/learn/courses/30/lessons/12932
# by riadjj@gmail.com
# --------------------------------------------------------

# my
n = 12345
n = str(n)
ans = []
for i in range(len(n), 0, -1) : 
    ans.append(int(n[i-1]))
print(ans)

# list reverse(list 타입 함수)
ans = list(str(n))
ans.reverse()
print(ans)

# list reversed(내장함수)
print(list(map(int, reversed(str(n)))))
