

b = '''
Is this the real life?
이게 진짜 현실일까?
Is this just fantasy?
단지 환상이 아닐까?
Caught in a landslide,
산사태에 파묻힌 것처럼,
No escape from reality 
현실에서 벗어날 수 없어
Open your eyes 
눈을 뜨고
Look up to the skies and see 
하늘을 올려다봐
I’m just a poor boy
난 그저 가난한 소년일 뿐이야
I need no sympathy 
동정은 필요하지 않아
Because I’m easy come, easy go, 
왜냐면 나는 쉽게 오고, 쉽게 가고
A little high, little low
조금 높고, 조금 낮게 사니까
Anyway the wind blows,
어찌됐든 바람은 불고,
Doesn’t really matter to me
나와는 관계 없는 일이지
To me...
나에게는...

Mama just killed a man
엄마, 사람을 죽였어요
Put a gun against his head
그의 머리를 향해 총을 들이대고
Pulled my trigger
방아쇠를 당겼어요
Now he`s dead!
그는 죽었어요!
Mama... Life had just begun
엄마... 삶이 이제야 시작됐었는데
But now I`ve gone and thrown it all away
하지만 내가 모든 것을 내던져버렸어요
Mama... wooo
엄마...
Didn`t mean to make you cry
당신을 울리고 싶었던게 아니었는데
If I`m not back again this time tomorrow
내가 내일 이 시간에 이곳으로 돌아오지 못하더라도
Carry on carry on
살아가세요 살아가세요
As if nothing really matters
아무 일도 없었던 것처럼
Too late
너무 늦었어
My time has come
내 차례가 와버렸는걸
Sends shivers down my spine
등골이 오싹해
Body`s aching all the time
몸이 계속해서 아파와
Goodbye, everybody
안녕히, 모두들
I`ve got to go
난 가야만 해요
Gotta leave you all behind
모든 것을 뒤로 하고
And face the truth
진실과 마주서야 해요
Mama... wooo
엄마...
I don`t want to die
죽고싶지 않아요
I sometimes wish I`d never been born at all
가끔 내가 태어나지 않았더라면 하고 바래요

I see a little silhouette of a man
한 남자의 실루엣이 보여
Scaramouche! Scaramouche!
겁쟁이! 겁쟁이!
Will you do the Fandango?
바보같은 짓을 할 셈이냐?
Thunderbolt and lightning
천둥과 번개가
Very very frightening me
나를 두렵게 해
Galileo, Galileo
갈릴레오, 갈릴레오
Galileo, Galileo
갈릴레오, 갈릴레오
Galileo figaro!
갈릴레오는 거짓말쟁이야
Magnifoco!
대단한 양반이지!

But I`m just a poor boy,
하지만 나는 가난한 소년일 뿐이고,
And nobody loves me
아무도 나를 사랑해주지 않지
He`s just a poor boy from a poor family
그는 가난한 집에서 태어난 가난한 소년일 뿐이에요
Spare him his life from this monstrosity
그를 괴물같은 삶에서 구해줍시다
Easy come easy go
쉽게 오고, 쉽게 가는게 삶이지
Will you let me go?
나를 놓아주겠어?
Bismillah! No, we will not let you go!
절대로! 안돼, 우린 너를 놔주지 않을거다!
Let him go!
그를 놔줍시다!
Bismillah! We will not let you go! Let him go!
절대로! 우린 너를 놔주지 않아! 그를 놔줍시다!
Bismillah! We will not let you go!
절대로! 우린 너를 놔주지 않아!
Let me go!
나를 놓아줘!
Will not let you go! Let me go!
너를 놔주지 않을 테다! 나를 놔줘!
Will not let you go! Let me go!
너를 놔주지 않아! 나를 놔줘!
No, no, no, no, no, no, no!
안돼, 안돼, 안돼, 안돼, 안돼, 안돼, 안돼!
Mama mia, mama mia. Mama mia, let me go!
엄마, 엄마. 엄마, 나를 놔주세요!
Beelzebub has a devil put aside for me
마왕이 내 옆에 악마를 보냈어요
For me,
나에게.
For me!
나를 위해!

So you think you can stone me and spit in my eye?
그래, 당신들이 나를 비난하고 내 눈에 침을 뱉을 수 있다 생각하나?
So you think you can love me and leave me to die?
당신들이 나를 사랑하면서 죽게 내버려둬도 된다 생각하나?
Oh Baby, Can`t do this to me baby
오, 내게 이럴 수는 없어
Just gotta get out
벗어나야 해
Just gotta get right outta here!
여기서 벗어나야만 해!

Nothing really matters
어느 것도 상관 없어
Anyone can see...
누구라도 알 수 있지,..
Nothing really matters
어느 것도 상관 없어
Nothing really matters
어느 것도 상관 없어
To me...
나에게는...

Anyway the wind blows...
어찌 됐든 바람은 불어...
'''

# 2)위의 가사에서 Mama가 추출된 횟수
def bohem(l):
    count = 0
    for i in range(len(l)):
        if l[i:i+4] == 'Mama':
            count += 1
    return count

print(bohem(b))
print(b.replace('mama','@@@@'))
# 3) 위의 가사에서 각각의 알파벳이 추출된 횟수
def bohemAlpha(l, a):
    count = 0
    for i in range(len(l)):
        if l[i] == a:
            count += 1
    return count
for i in range(97,123):
    print("%s는 %d회 추출되었습니다." %(chr(i),bohemAlpha(b.lower(), chr(i))))


# 4) jpg 파일 이름을 읽어 글자단위로 나누기

p = "20181110-171523.jpg"

def picRead(pic):
    print("촬영 날짜 : %s년 %s월 %s일" %(pic[:4],pic[4:6],pic[6:8]))
    print("촬영 시간 :","%s:%s:%s" %(pic[9:11],pic[11:13],pic[13:15]))
    print("확장자 : %s" %pic[16:])
picRead(p)

    





















