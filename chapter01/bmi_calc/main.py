


# age= input("당신의 나이는 몇 살입니까?>>>")
# print(type(age))
# print(f"당신은 내년에 {age+1}살이 됩니다.")-오류발생
'''
input() 함수의 결과값은 언제나 str입니다.

이때 필요한 함수가 '형변환 함수' 입니다.(conversion)
'''
# age1= input("당신의 나이는 몇 살 입니까?>>>")
# print(type(age1))     #결괴값:str
# age1_int= int(age1)   #str인 age1을 int 자료형으로 변환시켜서
#                       #age1_int라는 새로운 변수에 대입
# print(type(age1_int))
# print(f"당신은 내년에 {age1_int+1}살이 됩니다.")
'''
자주 쓰이는 형변환 함수
1. int() -> str 또는 float을 int로 변경
2. float-> str 또는 int를 float로 변경
3. round()-> 반올림 해주는 
'''
# temp= int(3,8)
# print(temp)
# temp2= float(4)
# print(temp2)
#
# temp3= round(3.8)
# print(temp3)

# temp4= round(5.3491285, 2) # 괄호 첫번재 수를 소수점 둘째 자리 까지 표기.
# print(temp4)
'''
BMI 계산기

1. 키를 입력받아(input()를 쓰라는 의미) 변수 height에 저장.
2. 몸무게를 입력받아 변수 weight에 저장
3. 몸무게/ 키의 제곱을 계산하면 bmi 지수가 나온다.
4. bmi 지수를 int로 출력.-> int()함수 사용.
5. bmi 지수를 소수점 셋째자리에서 반올림하여 둘째자리까지 출력.-> round()함수 사용

ex)
로고 출력하세요
당신의 키는 몇 cm입니까?>>>
당신의 몸무게는 몇 kg입니까>>>
당신의 bmi지수는 22입니다.
당신의 bmi지수는 22.xx입니다.'''


# height=input("당신의 키는 몇 cm입니까?>>>")
# height=float(height)   #str->float으로 변환
# height=height/100 #cm->m로 변환
# # height / 100
# # height_float=float(height)
# weight=input("당신의 몸무게는 몇 kg입니까?>>>")
# weight=float(weight)
# bmi= weight/ (height**2)
# bmi_int= int(bmi)  #int형으로
# bmi_round= round(bmi,2)
# print(f"당신의 bmi지수는 {bmi_int}입니다.")
# print(f"당신의 bmi지수는 {bmi_round}입니다.")
# print(logo)
# height= float(input("당신의 키는 몇 cm입니까?>>>"))/100
# weight= float(input("당신의 몸무게는 몇 kg입니까?>>>"))
# print(f"당신의 bmi지수는 {int(weight/(height**2))} 입니다.")
# print(f"당신의 bmi지수는 {round(weight/(height**2))} 입니다.")