# --------------------------------------------------------
# https://programmers.co.kr/learn/courses/30/lessons/12912
# by riadjj@gmail.com
# --------------------------------------------------------

a = int(input())
b = int(input())

if a==b:
    print(a)
elif a>b:
    a,b=b,a
print(sum(range(a,b+1)))