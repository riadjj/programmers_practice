# --------------------------------------------------------
# https://programmers.co.kr/learn/courses/30/lessons/12928
# by riadjj@gmail.com
# --------------------------------------------------------

n = 12
# 1 2 3 4 6 12
ans = 0

# 마이
for i in range(1, n+1) :
    if n%i == 0 :
        ans += i
print(ans)

# num/2 수들만 검사하는 경우
print(n + sum([i for i in range(1, (n // 2) + 1) if n % i == 0]))

# 풀어서 테스트
ans = 0
for i in range(1, n//2+1) :
    if n%i == 0 :
        ans += i
print(ans+n)