# --------------------------------------------------------
# https://programmers.co.kr/learn/courses/30/lessons/12936
# by riadjj@gmail.com
# --------------------------------------------------------

from math import factorial
n = 3
k = 5
myList = [i+1 for i in range(n)]
answer = []
while n!=0 :
    fact = factorial(n-1)
    answer.append(myList.pop((k-1)//fact))
    n -= 1
    k %= fact
print(answer)
