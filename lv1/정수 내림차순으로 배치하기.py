# --------------------------------------------------------
# https://programmers.co.kr/learn/courses/30/lessons/12933
# by riadjj@gmail.com
# --------------------------------------------------------

n = 118372
# my
n = str(n)
ans = []
for i in range(len(n)) : 
    ans.append(n[i])
ans.sort(reverse=True)
print(int(''.join(ans)))

# 리스트 생성 부분 공부할것
n = str(n)
ans = list(str(n))
ans.sort(reverse=True)
print (int(''.join(ans)))
