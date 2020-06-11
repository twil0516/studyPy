# 6)

member = []

def memMan():
    while not 0:
        print("1. 주소 추가")
        print("2. 주소 삭제")
        print("3. 주소 찾기")
        print("4. 주소 명단 확인")
        print("0. 종료")
        k = int(input("어떤 메뉴를 실행하시겠습니까 : "))
        if k == 1:
            memAdd()
        elif k == 2:
            memDel()
        elif k == 4:
            memPre()
        

def memPre():
    print()
    for i in range(len(member)):
        print("%d. %s" %(i+1, member[i]))
    print()

def memAdd():
    print()
    name = input("이름을 입력하세요 : ")
    pNum = input("번호를 입력하세요 : ")
    member.append(name+':'+pNum)
    print()
    print(member)
    print()
    
def memDel():
    print()
    x = int(input("몇번째 주소를 삭제하시겠습니까 : ")
    print()
    del(member(x))


memMan()

