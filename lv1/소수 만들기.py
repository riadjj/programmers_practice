# --------------------------------------------------------
# https://programmers.co.kr/learn/courses/30/lessons/12977
# by riadjj@gmail.com
# --------------------------------------------------------

def IsPrime(n) :
    if n <= 1 : 
        return False
    for i in range(2, n) : 
        if n%i == 0 : 
            return False
    return True

nums = [1,2,7,6,4]
answer = []

# 3개로 소수 만들어지는 경우의 수
# nC3
from itertools import combinations

combi = combinations(nums, 3)
for i,j,k in combi :
    if IsPrime(i+j+k) : 
        answer.append(i+j+k)
print(len(answer))