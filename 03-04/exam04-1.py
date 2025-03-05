def print_menu():
    print("##### 메뉴 #####")
    print("1. 명함 추가")
    print("2. 명함 전체 출력")
    print("3. 번호로 검색")
    print("4. 변경 사항 추가")
    print("5. 연락처 삭제")
    print("99. 종료")

def main():
    cards = [{'no': 1, 'name' : '홍길동', 'tel': '1234'},{'no': 2, 'name' : '전우치', 'tel': '5678'}]
    new_no = 3

    while True:
        print_menu()
        choice = input("메뉴 선택 :")
        if choice=='1':
            name = input("- 이름 입력 : ")
            tel = input('- 연락처 입력 : ')
            card = {'no':new_no, 'name':name, 'tel':tel}
            cards.append(card)
            new_no += 1

        elif choice==2:
            print(cards)
        elif choice==3:
            no = int(input('- 번호 입력 : '))
            for card in cards:
                if card['no']==no:
                    print(card)
                    break
        elif choice==4:
            pass
        elif choice==5:
            no = int(input('- 번호 입력 : '))
            for card in cards:
                if card['no']==no:
                    cards.remove(card)
                    break
        elif choice==99:
            print('사용해주셔서 감사합니다')
            break

main()