'''

Scope: 범위

지역 변수: 함수 내부에 정의된 변수
전역 변수: 함수 외부(main단계)에 정의된 변수
'''

# enemies=1       #전역 변수
#
# def increase_enemies():
#     enemies =2      # 같은 이름이지만 얘는 지역 변수에 해당
#     print(f"함수 내부의 적의 숫자는 {enemies}입니다.")
#
# increase_enemies()
# print(f"함수 외부의 적의 숫자는 {enemies}입니다.")

# 지역 변수 =/= 전역 변수-> 변수명을 서로 다르게 짓는게 혼란을 피하는 방식.

# 함수 정의
# def drink_potion():
#     potion_strength=2
#     print(potion_strength)

# drink_potion()
#print(potion_strength)  #오류 발생
# 지역 변수 선언-> 호출한다고 해서

'''
global scope
'''

# player_health=10
#
# def game():
#     # 함수 내부에 함수 정의
#     #함수 내에 정의를 새로 한다.
#     def drink_potion():
#         # player_health +=2        # 마찬가지로 전역에서 선언되고 초기화된 변수를
#                                 # 함수 내에서 조작하는것 불가능
#
#         # 근데 무조건 불가능은 아니다
#         global player_health    # global을 선언하고,
#         player_health +=2       # 값을 바꿀 전역 변수 명을 쓰게 되면
#         # 이상의 코드에서 생겨날 수 있는 잠재적인 문제점은:
#         #  함수의 호출 횟수에 따라 전역 변수의 값이 바뀌기 때문
#         #  전역 변수의 값을 정확히 알기 위해서 호출 횟수 알아야함
#
#
#     drink_potion()                            # 전역 변수의 값 바꿀 수 있음.
# game()
# print(f"체력은 {player_health}입니다.")
game_level=3
def create_enemy():
    enemies= ["좀비", "스켈레톤", "에일리언"]
    if game_level <5:
        new_enemy = enemies[0]

    print(new_enemy)

create_enemy()
'''
이상의 코드에서 생기는 문제점
1. gmae level 이라는 전역 변수를 create_enemy()라는 함수의 정의 부분에서 사용하고 있음에도 오류 발생하지 않음
2. 함수 정의 내부의 if절에서 new_enemy라는 변수를 선언 및 초기회 했음에도 불구하고
if절 바깥에서 new_enemy를 참조했음에도 오류가 발생하지 않음.

    1.의 이유: game_level이라는 전역변수의 값을 바꾸는게 아니라 참조만 해서 T/F만 반환-> 오류 발생 x
    2.의 이유: if/while/for 와 같이 콜론을 기준으로 들여쓰기가 있는 모든 코드 블록은 지역 변수를 만드는 것으로 간주 x
'''