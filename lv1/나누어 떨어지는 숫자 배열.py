# --------------------------------------------------------
# https://programmers.co.kr/learn/courses/30/lessons/12910
# by riadjj@gmail.com
# --------------------------------------------------------

arr = 	[2, 36, 1, 3]
divisor = 1
ans = []
for i in range(len(arr)) : 
    if arr[i]%divisor==0:
        ans.append(arr[i])
if not ans : 
    ans.append(-1)
ans.sort()
print(ans)