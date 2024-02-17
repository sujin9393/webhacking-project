def login(id, password):
    with open("users.txt", "r") as file: 
        for line in file: 
            saved_id, saved_password = line.strip().split(":") #파일에서 읽어온 문자열을 사용자 이름과 비밀번호로 분리해야됨 
            if id == saved_id and password == saved_password: 
                print("로그인 성공")
                return True 
    print("아이디 또는 비밀번호가 잘못되었습니다.")
    return False
        
def register(id, password):
    with open("users.txt", "a") as file:
        file.write(f"{id}:{password}\n") #사용자의 이름과 비밀번호를 ":"로 구분하여 한 줄에 저장하고 뒤에 \n 추가해서 줄 바꿈 
    print("회원가입이 완료되었습니다.")

def remove_user(id):
    with open("users.txt", "r") as file:
        lines = file.readlines() #파일에서 모든 줄을 읽어와서 각 줄을 리스트로 갖게 함 
    with open("users.txt", "w") as file: #쓰기 모드로 열어서 파일 내용 초기화 
        for line in lines: 
            if not line.startswith(id + ":"): #해당 줄이 사용자 이름과 :로 시작하지 않는지 확인 
                file.write(line) #삭제하려는 사용자 정보가 아니면 사용자의 정보를 파일에 다시 씀 
    print(f"사용자 '{id}'를 삭제하였습니다.")

def main():
    while True: 
        print ("1.로그인\t2.회원가입\t 3.사용자 탈퇴 \t 4. 종료 ")
        number = input("메뉴를 선택하세요:")

        if number == '1':
            id = input("아이디를 입력하세요: ")
            password = input("비밀번호를 입력하세요: ")
            login(id, password)
        elif number =='2': 
            id = input("아이디를 입력하세요: ")
            password = input("비밀번호를 입력하세요: ")
            register(id, password)
        elif number == '3': 
            id = input("삭제할 아이디를 입력하세요: ")
            remove_user(id)
        elif number == '4':
            print("프로그램을 종료합니다.")
            break


main()