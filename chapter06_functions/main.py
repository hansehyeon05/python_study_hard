'''

1. 함수(function) : 특정 작업을 수행하는 코드 블록을 정의하는 방법

예) '사진을 찍는다'라는 행위에 대해 생각.
1) 주머니에서 폰을 꺼내고,
2) 잠금 화면을 풀고,
3) 카메라를 켜고,
4) 사진을 찍고자 하는 대상에 폰을 조준하고,
5) 셔터를 누른다.

라고 볼 수 있다. 그런데 컴퓨터는 시키는대로만 하기 때문에 사진을 찍기 위해서
1)-5)까지의 명령어를 입력해줘야 한다.

하지만 '사진을 찍는다'라는 함수 내에 1)-5)의 명령어들을 미리 입력.
'사진을 찍는다'라는 명령어 실행-> 1)-5)까지의 명령들을 순서대로 수행하도록 하는 것

함수 정의 형식:
def turn_right():
    turn_left()
    turn_left()
    turn_left()


함수 호출 형식:
turn_right()

2. 함수의 종류
`   1) 파이썬 내장 함수
    2) 메서드
    3) 사용자 정의 함수


3. 함수 용어 정리
    1) 함수 정의: 사용자 함수를 만드는것.(def)
    2) 인수: 함수에 전달할 입력값
    3) 매개변수: 인수를 받아서 저장하는 변수를 의미
    4) 반환값/결과값/리턴값 : 함수의 출력값
    5) 함수 호출: 함수를 실제로 사용하는 것을 의미


4. 사용자 함수의 형식:
def 함수_이름(매개변수):
    실행문

변수= 함수_이름()
'''
# 함수 정의
# def write_name(name):               # 정의할 때 소괄호 내:parameter
#     print(f"당신의 이름은 {name}입니다.")
#
# #함수 호출
# write_name("한세현")                   # 호출할 때 소괄호 내: arguement
#
# def write_name_age(name,age):
#     print(f"당신의 이름은 {name}이고, 나이는 {age}살입니다.")
#
# write_name_age("한세현", 38)
# write_name_age(age=10, name="한세현")
'''
우리가 예를 들어 input("이름을 입력하세요>>>")을 이용해서 이것을 name이라는 변수에 담았다고 가정하면,
nmae=input("이름을 입력하세요>>>")이라고 직성해왔다.

파이썬 내장 함수는 이미 함수가 정의 돼있고 개발자들은 함수 호출만 잘하면 된다.
사용자 함수는 개발자 자신이 함수를 정의, 그 후에 호출하는 것까지의 과정이라고 생각하면 된다.

내장 함수 예)
print()/ type()/ int()/ flat()/ input()

2. 메서드: 특정 객체가 가지고 있는 함수를 의미. 특정 자료형에 포함돼있는 함수.
사실 함수와 메서드는 동일한 개념이지만, 호출 방식에 있어서의 차이가 있습니다.

함수는 독립적으로 사용 가능/ 메서드의 특정 객체를 통해서만 호출 가능
'''
# eng_name= input("당신의 이름을 소문자로 입력하세요.>>>").upper()
# #이상의 코드에서 input()은 함수, .upper()은 메서드
# print(eng_name)#함수
# eng_name2= input("당신의 이름을 소문자로 입력하세요.>>>").title()
# print(eng_name2)
'''
함수(메서드)의 유형
'''
# def call1():
#     print("[x | x]")
#
# def call2(str_type):
#     print("[o | x]")
#     print(f"{str_type}이라고 입력하셨나보네요.")
#
# def call3():
#     print("[x | o]")
#     return 1
#
# def call4(str_type):
#     print("[x | o]")
#     return f"제 이름은 {str_type}입니다."
#
# call1()
# call2("오늘 날씨 너무 추워요")
# call3() # 이 경우 return이 출력 안됨.
# print(call3())  # 이 경우에만 return이 출력된다.
# print(call3()+1)
#
# new_element = (call3()+3)*10
# print(new_element)
#
# print(call4("한세현"))
'''
call3()/call4() 유형에서 함수 내에 print()를 집어넣으면 main 단계에서 (들여쓰기가 되어있지 않은 단계)
print() 함수를 입력할 필요가 없어 휠씬 편함
굳이 return 형태로 입력해야 하는가?

함수형 프로그래밍 : 특정한 함수1의 결과값이 
또 다른 함수2의 arguement로 사용되는 것을 의미한다.
그리고 함수2의 결과 값이 함수3의 arguement로 사용되는 것이 반복된다면,

'''

#사용자 함수 정의
# def introduce(name, address):
#     return f"제 이름은 {name}이고, {address}에 삽니다."
#
# #함수 1의 사용: input()
# name=input("이름을 입력하세요>>>")
# address=input("주소를 입력하세요>>>")
#
# # 함수 1의 결과값을 함수2인 사용자 함수의 arguement로 사용-> 그 결과를 함수3인 print()함수의 arguement로 사용.
# print(introduce(name, address))

'''
700원 짜리 음료수를 뽑을 수 있는 자판기 프로그램을 구현하시오. 돈을 넣으면 몇 잔의 음료수를 뽑을 수 있는 지, 그리고 잔돈은 얼마인지 
모든 경우의 수를 출력하도록 합니다.

함수 정의
-반환값: 없음(call-4중 어떤 유형일지 고려하세요)
-함수 이름: vending_machine()
-.매개 변수: 정수 money

코드 구성

def vending_machine():

vending_machine(3000)

예)
음료수=0개, 잔돈=3000원
음료수=1개, 잔돈=2300원
음료수=2개, 잔돈=1600원
음료수=3개, 잔돈=900원
음료수 4개, 잔돈=200원
'''



# my_money=3000
# drink_price=700

# charge=3000-(700*음료수 개수)

# for i in range(int(my_money//drink_price)+1):         # /:나머지, //:몫, %:나누기
#     print(f"음료수= {i}개, 잔돈= {my_money-(drink_price*i)}")

# def vending_machine(money):
#     for i in range(money//700+1):
#         print(f"음료수= {i}개, 잔돈= {money-(700*i)}")
#
#
# #함수 호출
# vending_machine(5000)

'''
예제: 구구단 출력

함수 정의:
함수이름: multiply
매개변수: 정수 n

함수 호출:
multiply(dan)

예)
몇 단을 출력하시겠습니까?>>> 3
3x1=3
...
3x9=27
'''
# 함수 정의-> call2유형
# def multiply(n):
#
#     for i in range(1,10,1):
#         print(f"{dan}x{i}={dan*i}")
# dan=int(input("몇 단을 출력하시겠습니까?>>>"))
#
# multiply(dan)

# 함수 정의-> call1
# def multiply2():
#     dan=int(input("몇 단을 출력하시겠습니까?>>>"))
#     for i in range(1, 10, 1):
#         print(f"{dan}x{i}={dan * i}")

# print(dan)          #오류-> 함수를 정의만 하는 것은 사용한 게 아니기 때문에 변수에 해당하지 않음
# dan=3               # 그리고 structure를 확인한 결과 선언한 dan이 없음.



