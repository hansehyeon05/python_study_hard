'''
지시 사항

사용자에게 전체 음식값($), 몇 %의 팁을 낼 것인지, 인원수를 입력받을 예정입니다.

예)

음식 가격은 얼마입니까?>>>200
몇 퍼센트(%)의 팁을 내실 예정입니까, 10, 12, 15% 중에서 선택하세요. >>> 10
몇 명의 인원이 나누어 내나요?>>>5

당신이 내야할 전체 음식 금액은 $44.0달러 입니다.
'''

# food=float(input("음식 가격은 얼마입니까?>>>$"))
# percent= float(input("몇 퍼센트(%)의 팁을 내실 예정입니까?>>>"))
# people= int(input("몇 명의 인원이 나누어 내나요?>>>"))

#percent가 10,12,15중에 하나니까 예를 0.1, 0.12, 0.15로 바꿀 필요 있음


# percent= percent/100
# tip=food*percent
# total_price= food+ tip
# price_per_person= total_price /people
# price_per_person= round(price_per_person,2)


# print(f"당신이 내야 할 전체 음식 금액은 ${price_per_person}달러 입니다")

#짧은 버전
food= float(input("음식 가격은 얼마입니까?>>>$"))
percent= float(input("몇 퍼센트(%)의 팁을 내실 예정입니까,10,12,15%중에서 선택하세요. >>>"))/100
people= int(input("몇 명의 인원이 나누어 내나요?>>>"))
print(f"당신이 내야 할 전체 금액은 ${round((food*(1+percent))/people,2)}입니다.") # food*(1+percent)
print(f"당신이 내야 할 전체 금액은 ${((food*(1+percent))/people):.2f)}입니다.")
#36번 라인의 경우는 round()함수와 달리 어떤 상황에서도 소수점 둘째자리까지 표기되도록 강제하는 코드

'''
우클릭-> new-> package-> 이름-> 우클릭-> 파이썬 파일'''
