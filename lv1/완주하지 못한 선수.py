# --------------------------------------------------------
# https://programmers.co.kr/learn/courses/30/lessons/
# by riadjj@gmail.com
# --------------------------------------------------------

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
answer = 0

# 시간 초과 
# for comp in completion : 
#     participant.remove(comp)
# print(''.join(participant))

# 중복 걸리네
# for user in participant : 
#     if user not in completion : 
#         print(user)

# 딕셔너리? 통과는 했는데 느리네 : 최대 52.03m ~ 58
# my
dict = {}
for player in participant : 
    if player not in dict : 
        dict[player] = 1
    else :
        dict[player] += 1
for comp in completion : 
    dict[comp] -= 1
for k, v in dict.items() :
    if v == 1 :
        print(k)


# other 최대 : 57.06ms???? 
answer = ''
temp = 0 
dic = {}
# 해쉬 값 다 더하기
for part in participant:
    dic[hash(part)] = part
    temp += int(hash(part))

# 해쉬 값 차감
for com in completion:
    temp -= hash(com)

# 남는 해쉬 값으로 dic 출력
answer = dic[temp]
print(answer)