'''
while 반복문( 조건문이 False가 될때까지 실행.)

형식:
while 조건문:
    실행문:
'''
#무한 루프의 개념
# num=1
# while num>0:
#     print(num)

'''
그래서 while 반복문을 작성할 때 고려할 점:
    특정한 상황에서 조건식이 거짓이 될 수 있도록 사전에 미리 지정해줘야함.
    -> 아닐 경우 무한 루프에 빠지게 됨
    '''

# num2=1
# while num2 <11:
#     print(num2)
#     num2+=1   #조건문이 거짓이 되도록하는 부분
#
# print(f"최종 num2는 {num2}")
'''
if문과의 비교
if문의 경우 조건식이 참일때 실행문이 한번 실행.
while문의 경우 조건문이 참일 때 실행문이 '반복' 실행

예제
10부터 1 까지의 모든 정수 출력'''

# num3=10
# while num3> 0:
#     print(num3)
#     num3-=1

# num3=11
# while num3>1:
#     num3-=1
#     print(num3)

'''

중첩 while문(Nasted while-loop):while 내부에 while문 나타남.

예)
총 5일동안 매일 3시간씩 수업을 진행합니다. 매일 '1일차 1교시입니다.'와 같은 메시지를 출력합니다.

1일차 1교시입니다.
1일차 2교시입니다.
1일차 3교시입니다.
...'''

# day=1
# while day<6:
#     hour=1
#     while hour<4:
#         print(f"{day}일차 {hour}교시입니다.")
#         hour+=1       #내부 반복 먼저 -> 내부 반복 끝나면 day가 하나 증가 (들여쓰기 중요)
#     day +=1

'''
예제)

구구단 2단부터 9단까지 출력하는 프로그램 작성.
변수명은 dan / number

2x1=2
2x2=4
2x3=6
...
9x8=72
'''

# dan=2
# while dan<10:          #값이 있으면 T로 취급함
#     number=1
#     while number<10:
#         print(f"{dan}x{number}={dan*number}")
#         number+=1
#     dan+=1

# num=1
# while num <101:
#     print(f"{num} {num+1} {num+2} {num+3} {num+4} {num+5} {num+6} {num+7} {num+8} {num+9} ")
#     num+=10

#이상의 코드의 경우에는 반복을 10번 돌리는 경우였습니다.
# n2=1
# while n2 <101:
#     print(n2, end=" ")
#     if n2 % 10==0:
#         print()
#     n2+=1






