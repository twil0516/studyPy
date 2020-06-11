
while True:
    a = int(input("1. 주차\n2. 출차\n3. 남은 주차공간 개수\n4. 종료\n"))
    b = 10
    if a == 1:
        b = b - 1
        print('주차가 완료되었습니다.\n')
    elif a == 2:
        b = b + 1
        print('안녕히가십시오.\n')
    elif a == 3:
        print('주차공간이 %d자리 남았습니다.\n' %b)
    elif a == 4:
        print("시스템을 종료합니다.\n")
        break
          
