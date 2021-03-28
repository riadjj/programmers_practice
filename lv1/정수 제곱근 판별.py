# --------------------------------------------------------
# https://programmers.co.kr/learn/courses/30/lessons/12934
# by riadjj@gmail.com
# --------------------------------------------------------

# import math
n=25
# ans=math.sqrt(n)
ans=n**(1/2) #제곱근 함수 안 쓰고 처리가능하네
if ans%1==0:
      ans = (ans+1)**2
else :
      ans = -1
print(int(ans))