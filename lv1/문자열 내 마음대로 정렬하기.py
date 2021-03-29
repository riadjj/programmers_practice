# --------------------------------------------------------
# https://programmers.co.kr/learn/courses/30/lessons/12915
# by riadjj@gmail.com
# --------------------------------------------------------

import operator

# strings = ["sun", "bed", "car"]
# n = 1
# # ["car", "bed", "sun"]

strings = ["abce", "abcd", "cdx"]
n = 2
# ["abcd", "abce", "cdx"]
answer = []

# my
strings.sort()
tmp = {}
for str in strings : 
    tmp[str] = str[n]
tmp = sorted(tmp.items(), key=operator.itemgetter(1))
for s in tmp :
    answer.append(s[0])
print(answer)

# other1
print(sorted(sorted(strings), key=lambda x:x[n]))

# other2
print(list(sorted(strings, key=lambda x : (x[n], x.lower()))))

