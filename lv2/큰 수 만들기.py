# --------------------------------------------------------
# https://programmers.co.kr/learn/courses/30/lessons/
# by riadjj@gmail.com
# --------------------------------------------------------

number = '111188899994177252841'
k = 10
# 775841

# my
answer = ''
maxLenth = len(number)-k
max, pin = 0, 0
while len(answer) != maxLenth :
    for i in range(pin, len(number)-maxLenth+len(answer)+1) :
        if number[i] == '9' :
            max = 9
            pin = i+1
            break
        elif int(number[i]) > max :
            max = int(number[i])
            pin = i+1
    
    answer += str(max)
    max = 0

print(answer)

# other use stack...
stack = [number[0]]
for num in number[1:]:
    while len(stack) > 0 and stack[-1] < num and k > 0:
        k -= 1
        stack.pop()
    stack.append(num)
    print(stack)
if k != 0:
    stack = stack[:-k]
print(''.join(stack))