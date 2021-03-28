# --------------------------------------------------------
# https://programmers.co.kr/learn/courses/30/lessons/12943
# by riadjj@gmail.com
# --------------------------------------------------------

n=626331
ans=0

while 1 :
      if n == 1:
            break
      elif ans >= 500:
            ans = -1
            break
      elif n%2 == 0:
            n = n/2
            ans += 1
      else :
            n = n*3+1 
            ans += 1
print(ans)