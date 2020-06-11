# 함수
#--> 소스 코드의 블럭에 이름을 붙여 정의하고 사용하는 것
#--> 자주 반복적으로 사용되는 코드를 호출
#--> 호출을 통해 실행 !!

#def 함수이름 ( 매개변수 ):
#    실행코드
#    return x

# calcsum : 1에서 자기자신까지의 모든값을 더하는 함수

def CalcSum(n):
    sum = 0
    for i in range(n+1):
        sum += i
    return sum

#        호출
#print(CalcSum(5))

# 매개변수 (인수, 인자, 파라미터)
#--> 호출하는 곳에서 함수로 전달해주는 값

def CalcRange(begin, end):
    sum = 0
    for i in range(begin, end+1):
        sum += i
    return sum
#print( CalcRange(3, 5) )

# 리턴 값 : 함수의 실행결과를 호출한 곳으로 되돌려주는 값
#--> 항상 리턴 값이 존재하는 것은 아니다!!
# ex) 정수 1개를 매개변수로 전달받아 1 ~ 정수까지를 출력 !!
def printN(n):
    for i in range(n+1):
        print(i,end = '')
#printN(5)


#=========================================================
# 가변 인수
#--> 매개변수의 갯수가 동적인 경우 사용 !!
#=========================================================

# 정수들의 합계를 리턴하는 함수
def intSum( *n ): # * : 개별 변수값들이 하나의 list로 변환되어 전달 !!
    sum = 0
    for i in n:
        sum += i
    return sum

print(intSum(10,20,30,40,50,60,70,80))

#def strSum( s, *n ):  # *가 들어간 가변인수는 항상 마지막 인수로 전달 !!
#    print(s, n)

#strSum('aaa',10,20,30)

# CalcRange : 범위만큼 출력
# 기본 매개변수 값( 디폴트 파라미터 )
def CalcRangeStep( begin = 0, end = 10, step = 1):
    for i in range( begin, end + 1, step):
        print(i, end = '')

CalcRangeStep(5)

def Range (begin = 0; end, step = 1):
    




















