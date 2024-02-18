# my_set = {1, 2, 3, 3, 3}
# print(my_set)

# java = {"유재석", "김태호", "양세형"}
# python = set(["유재석", "박명수"])

# #교집합 (java & python 모두 할 수 있는 사람)
# print(java & python)

# #합집합
# print(java | python)

# #차집합 (java o , python x)
# print(java - python)

# #python 할 줄 아는 사람 추가
# python.add("김태호")
# print(python)

# #삭제
# java.remove("양세형")
# print(java)

# 자료 구조의 변경
#커피숍

menu = {"커피", "우유", "주소"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))