# --------------------------------------------------------
# https://programmers.co.kr/learn/courses/30/lessons/12945
# by riadjj@gmail.com
# --------------------------------------------------------

n = 7

def fibon(n) : 
    a = b = 1
    result = []
    for i in range(n) : 
        result.append(a)
        a, b = b, a + b
    return result

answer = fibon(n)
print(answer[n-1] % 1234567)
