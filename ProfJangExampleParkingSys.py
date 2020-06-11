# 5)
car = [0,0,0,0]

carno = 1234

def menu():
    while not 0:
        print("1. 현 상태")
        print("2. 입차")
        print("3. 출차")
        print("0. 종료")
        
        Input = int(input("메뉴를 선택해 주십시오 : "))
        
        if Input == 1:
            pre()
            
        elif Input == 2:
            carEnter()
            
        elif Input == 3:
            carExit()
            
        elif Input == 0:
            print("종료합니다")
            break
        
        else:
            print()
            print("다시 입력해주십시오.")
            print()

def pre():
    print()
    for i in car:
        print("[%d]" %i, end = '')
    print()
    print()

def carEnter():
    x = int(input("몇번 자리에 입차하시겠습니까? : "))
    no = int(input("차량번호를 입력해주세요 : "))
    car[x-1] = no
    print()
    print("%d번 차량이 %d번 자리에 입차했습니다" %(no,x))
    print()
    pre()
    print()
    
    
def carExit():
    x = int(input("현재 주차되어있는 자리를 입력해주세요 : "))
    no = car[x-1]
    car.remove(no)
    car.insert(x-1, 0)
    print()
    print("%d번 차량이 출차했습니다" %no)
    print("%d번 자리가 비었습니다" %x)
    print()
    pre()

menu()






























