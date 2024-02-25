f = open("새파일.txt", 'w')

for i in range(1, 11): #1부터 10까지 i에 대입
	data = "%d번째 줄입니다.\n" %i
    f.write(data)
f.close()


#수정 후 