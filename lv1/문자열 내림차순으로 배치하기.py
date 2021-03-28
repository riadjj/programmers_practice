# --------------------------------------------------------
# https://programmers.co.kr/learn/courses/30/lessons/12917
# by riadjj@gmail.com
# --------------------------------------------------------

s = "Zbcdefg"

ans = list(str(s))
ans.sort(reverse=True)
print(''.join(ans))

# 한줄로
print(''.join(sorted(s, reverse=True)))
