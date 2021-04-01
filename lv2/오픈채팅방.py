# --------------------------------------------------------
# https://programmers.co.kr/learn/courses/30/lessons/42888
# by riadjj@gmail.com
# --------------------------------------------------------

record = ["Enter uid1234 Muzi",
 "Enter uid4567 Prodo",
 "Leave uid1234",
 "Enter uid1234 Prodo",
 "Change uid4567 Ryan"]
answer = []

logs = [r.split(' ') for r in record]
udb = {log[1]:log[2] for log in logs if len(log)==3}

for log in logs :
    if log[0] == 'Enter' :
        answer.append('{}님이 들어왔습니다.'.format(udb[log[1]]))
    elif log[0] == 'Leave' :
        answer.append('{}님이 나갔습니다.'.format(udb[log[1]]))

print(answer)