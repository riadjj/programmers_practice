# --------------------------------------------------------
# https://programmers.co.kr/learn/courses/30/lessons/12901
# by riadjj@gmail.com
# --------------------------------------------------------

a = 5
b = 24
answer = ''

# my
dayString = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT',]
monthPerDay = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
checkDay = 0
for i in range(0, a-1) : 
    checkDay += monthPerDay[i]
checkDay += b
answer = dayString[(checkDay+4)%7]
print(answer)

# other 1
import datetime
t = 'MON TUE WED THU FRI SAT SUN'.split()
print(t[datetime.datetime(2016, a, b).weekday()])

# other 2
answer = ''
day = ['THU','FRI','SAT','SUN','MON','TUE','WED']
month = [31,29,31,30,31,30,31,31,30,31,30,31]
stack_day = sum(month[:a-1])+b #sum 활용법 체크
answer= day[stack_day%7]
print(answer)