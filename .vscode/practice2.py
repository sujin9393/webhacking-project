# print("Python", "Java", sep=",",end="?")
# print("우와!")


# # 시험 성적 
# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items():
#     # print(subject, score)
#     print(subject.ljust(5), str(score).rjust(4),sep=":")

# sentence = input("문자열을 입력하시오: ")

# def check_sentence(s):
#     if len(s)>=0


# def intro():
#      print('Hello my name is sujin') #긴 코드를 intro라는 단어로 축약한 것, 짧은 함수 단축키?






def wordsCount(text): 
    words = text.split() #문자열을 공백을 기준으로 나누어 리스트로 만듬 
    return len(words) #리스트의 길이를 반환하여 단어 수 세어줌 

input_text = input("문자열을 입력하세요: ") #입력 문자열 받기 
print("입력한 문자열의 단어 수는 " + wordsCount(input_text)) #wordsCount 함수에서 단어 수 세고 출력 