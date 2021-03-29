# --------------------------------------------------------
# https://programmers.co.kr/learn/courses/30/lessons/12940
# by riadjj@gmail.com
# --------------------------------------------------------

n=2
m=5
answer = []

# math 사용
from math import gcd
def lcm(X, Y):
    return (X*Y) // gcd(X, Y)

# 구현
def GCD(X, Y):
    while(Y):
        X, Y = Y, X%Y
    return X
def LCM(X, Y):
    return (X*Y) // GCD(X, Y)

print([gcd(n, m), lcm(n, m)])