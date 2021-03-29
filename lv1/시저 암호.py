# --------------------------------------------------------
# https://programmers.co.kr/learn/courses/30/lessons/12926
# by riadjj@gmail.com
# --------------------------------------------------------

s = "a B z"
n = 4
answer = ''

# A 65 ~ Z 90
# a 97 ~ z 122

# my
for c in s : 
    ans = ord(c)+n
    if c == ' ':
        answer += ' '
        continue
    elif c.isupper() and ans > ord('Z') :
        ans = ans-26
    elif ans > ord('z') :
        ans = ans-26
    answer += chr(ans)
print(answer)

# other
answer = ''
for i in s:
    if i >= 'A' and i <= 'Z':
        answer += chr((ord(i) - ord('A') + n) % 26 + ord('A'))
    elif i >= 'a' and i <= 'z':
        answer += chr((ord(i) - ord('a') + n) % 26 + ord('a'))
    else : answer += ' '
print(answer)