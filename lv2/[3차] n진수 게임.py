# --------------------------------------------------------
# https://programmers.co.kr/learn/courses/30/lessons/17687
# by riadjj@gmail.com
# --------------------------------------------------------

def numberal(number, base) : 
    q, r = divmod(number, base)
    n = '0123456789ABCDEF'[r]
    return numberal(q, base) + n if q else n

n = 2
t = 4
m = 2
p = 1

answer = ''
result = []
num = 0
while 1:
    str = numberal(num, n)
    for j in str : 
        result.append(j)
    if len(result) > t*m:
        break
    num += 1
        
for i in range(len(result)) : 
    if i%m == p-1 :
        answer += result[i]
        
print (answer[0:t])
