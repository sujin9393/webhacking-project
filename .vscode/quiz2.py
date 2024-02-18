# Quiz) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다. 
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다. 
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다. 
# 추첨 프로그램을 작성하시오. 

# 조건1: 편의상 댓글은 20명이 작성, 아이디는 1~20이라고 가정 
# 조건2: 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가 
# 조건3: random 모듈의 shuffle과 sample 활용 

#간단 과정 
# from random import *
# list = [1,2,3,4,5]
# shuffle(list) #번호 셔플
# print(list)
# print(sample(list,1)) #리스트 중에서 랜덤으로 하나 뽑음 

from random import *
users = range(1, 21) #1부터 20까지 숫자 생성 
users = list(users)
print(users)
shuffle(users)
print(users)

winners = sample(users, 4) #4명 뽑기 

print("--당첨자 발표--")
print("치킨 당첨자: {0}".format(users[0]))
print("커피 당첨자: {0}".format(users[1:4]))
print("--축하합니다--")
