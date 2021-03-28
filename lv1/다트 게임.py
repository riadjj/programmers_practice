# --------------------------------------------------------
# https://programmers.co.kr/learn/courses/30/lessons/17682
# by riadjj@gmail.com
# --------------------------------------------------------

# re 활용한 정규식 참고용
import re

dartResult = '1D2S3T*'
bonus = {'S' : 1, 'D' : 2, 'T' : 3}
option = {'' : 1, '*' : 2, '#' : -1}
p = re.compile('(\d+)([SDT])([*#]?)')
dart = p.findall(dartResult)   
# [('1', 'D', ''), ('2', 'S', ''), ('3', 'T', '*')]

for i in range(len(dart)):
    if dart[i][2] == '*' and i > 0:
        dart[i-1] = dart[i-1] * 2
    dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]
    # ('1', 'D', '') => 1     # ('2', 'S', '') => 2    # ('3', 'T', '*') => 54
answer = sum(dart)
print(answer) # 54



# 내 답안 : 문자열 변환을 통한 계산식 생성 후 처리
data = '1D2S3T*'
data = data.replace('*', '!')
data = data.replace('S#', '*(-1) ')
data = data.replace('D#', '**2*(-1) ')
data = data.replace('T#', '**3*(-1) ')
data = data.replace('S', ' ')
data = data.replace('D', '**2 ')
data = data.replace('T', '**3 ')
tmp = list(map(str, data.split()))

for i in range(len(tmp)) :
    for j in range(len(tmp[i])) : 
        if tmp[i][j] == '!':
            if i == 1 :
                tmp[i-1] = tmp[i-1] + '*2'
            elif i >= 2 : 
                tmp[i-1] = tmp[i-1] + '*2'
                tmp[i-2] = tmp[i-2] + '*2'

form = '+'.join(tmp)
form = form.replace('!', '')
if form[-1] == '+' :    form = form[:-1]
print(form)
print(eval(form))

