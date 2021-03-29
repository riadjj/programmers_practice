# --------------------------------------------------------
# https://programmers.co.kr/learn/courses/30/lessons/12919
# by riadjj@gmail.com
# --------------------------------------------------------

seoul = ["Jane", "Kim"]	
answer = 0

# my
for i in range(len(seoul)) :
    if seoul[i] == 'Kim' :
        answer = i
        break;
print('김서방은 %d에 있다' %answer)
print('김서방은 {}에 있다'.format(answer))

# other 
print("김서방은 {}에 있다".format(seoul.index('Kim')))