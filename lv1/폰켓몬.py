# --------------------------------------------------------
# https://programmers.co.kr/learn/courses/30/lessons/
# by riadjj@gmail.com
# --------------------------------------------------------

nums = [3,1,2,3]
# 2

answer = 0

# my
answer = min(int(len(nums)/2), len(set(nums))) 
print(answer)

# other //2 몫 으로 처리했네
answer = min(len(set(nums)), len(nums)//2)
print(answer)

# test
print(6/2)
print(6//2)