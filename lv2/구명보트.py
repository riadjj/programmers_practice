# --------------------------------------------------------
# https://programmers.co.kr/learn/courses/30/lessons/42885
# by riadjj@gmail.com
# --------------------------------------------------------

people = [10, 20, 30, 70, 80, 90, 100, 50]
limit = 100
answer = 0

people.sort()

# my first
answer = 0
si = 0
ei = len(people)

while 1 : 
    lenth = ei - si
    if lenth <= 0 :
        break

    a = people[si] 
    b = people[ei-1]
    ei -= 1

    if b <= limit/2 and lenth > 1 : 
        answer += int(lenth/2)
        if lenth%2 == 1:
            answer += 1
        break

    if b+a <= limit and lenth > 1:
        si += 1
        answer += 1
    else : 
        answer += 1

print(answer)


# other 참고해서 간략화 작업
answer = 0
first = 0
last = len(people)-1

while first<last : 
    if people[first]+people[last] <= limit :
        first += 1
    last -= 1
    answer += 1
    if first == last:
        answer += 1

print(answer)

# other 뭐가 다르지
answer = 0
a = 0
b = len(people) - 1
while a < b :
    if people[b] + people[a] <= limit :
        a += 1
        answer += 1
    b -= 1
print(len(people)-answer)