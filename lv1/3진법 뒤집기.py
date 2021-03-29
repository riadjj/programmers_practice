# --------------------------------------------------------
# https://programmers.co.kr/learn/courses/30/lessons/68935
# by riadjj@gmail.com
# --------------------------------------------------------

n = 229
# my
def numberal(number, base) : 
    q, r = divmod(number, base)
    n = '0123456789ABCDEF'[r]
    return numberal(q, base) + n if q else n
answer = 0
tmp = numberal(n, 3)

#문자열 역순 및 int 활용해서 바로 만들기
print(int(tmp[::-1], 3))

# 수동으로 계산
for i in range(len(tmp)) :
    answer += (int(tmp[i]) * 3**i)
print(answer)

# other
tmp = ''
answer = 0
while n >= 1:
    remainder = n % 3
    tmp += str(remainder)
    n = n // 3
answer = int(tmp, 3) 
print(answer)
