#=========================================================
# 반복문
#--> 코드의 일부분을 반복적으로 실행
#--> 루프 : 반복적인 실행 !!
# 초기값, 조건, 증감
#--> foreach ==> java, C#
#=========================================================
# 문법           //초기값, 조건
#for 변수 in range(1    , 5)

#for( int i = 1; i < 5; i++) --> C / JAVA

#for x in range(1,5):
#    print(x, end='')
# 1 ~ 10 의 수중에 짝수의 합 !!

sum = 0

#for i in range(1, 11):
#    if i % 2 == 0:
#        sum+=i
#print(sum)

#while
#i = 1
#while i <= 10:
#    if not i % 2:
#        sum+=i
#    i+=1
#print(sum)

# break 구문
#--> 반복문 탈출 (종료)
# ex) score 리스트에서 80을 찾아라
score = [92, 59, 89, 80, 70]

print(score)
# for( int i = 0; i < 5; i++)
#     print( score[i] );
# continue : 이번 반복만 종료하고 다음으로 !!
for i in score:
    if( i == 80 ):
        continue
    print(i)
#=========================================================
# 구구단
for dan in range (2,10):
    print('%d단' %dan)
    for hang in range (2, 10):
        print(dan, '*',hang, '=',dan * hang)
    print()

dan = 2
while dan <= 9:
    hang = 2
    while hang <= 9:
        print(dan, '*',hang, '=',dan * hang)
        hang += 1
    print()
    dan += 1




















