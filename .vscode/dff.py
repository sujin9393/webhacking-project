def register_user(username, password):
    with open("users.txt", "a") as file:
        file.write(f"{username}:{password}\n")
    print("회원가입이 완료되었습니다.")

def remove_user(username):
    with open("users.txt", "r") as file:
        lines = file.readlines()
    with open("users.txt", "w") as file:
        for line in lines:
            if not line.startswith(username + ":"):
                file.write(line)
    print(f"사용자 '{username}'를 삭제하였습니다.")

def login(username, password):
    with open("users.txt", "r") as file:
        for line in file:
            stored_username, stored_password = line.strip().split(":")
            if username == stored_username and password == stored_password:
                print("로그인 성공!")
                return True
    print("아이디 또는 비밀번호가 잘못되었습니다.")
    return False

def main():
    while True:
        print("\n1. 회원가입\n2. 로그인\n3. 사용자 탈퇴\n4. 종료")
        choice = input("메뉴를 선택하세요: ")

        if choice == '1':
            username = input("사용자 이름을 입력하세요: ")
            password = input("비밀번호를 입력하세요: ")
            register_user(username, password)
        elif choice == '2':
            username = input("사용자 이름을 입력하세요: ")
            password = input("비밀번호를 입력하세요: ")
            login(username, password)
        elif choice == '3':
            username = input("삭제할 사용자 이름을 입력하세요: ")
            remove_user(username)
        elif choice == '4':
            print("프로그램을 종료합니다.")
            break
        else:
            print("올바른 메뉴를 선택하세요.")

if __name__ == "__main__":
    main()