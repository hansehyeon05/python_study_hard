height= float(input("당신의 키는 몇 cm입니까?>>>"))/100
weight= float(input("당신의 몸무게는 몇 kg입니까?>>>"))
# print(f"당신의 bmi지수는 {int(weight/(height**2))} 입니다.")
bmi= round(weight/(height**2))

print(f"당신의 bmi지수는 {round(weight/(height**2))} 입니다.")

'''
업그레이드 관련 지시 사항

1. chrome에서 bmi가 특정 구간일 때 마다
당신의 bmi 지수는 xx.xx이고, 저체중/정상/과체중/비만입니다.
'''

if bmi <18:
    print("저체중입니다.")
elif bmi <23.5:
    print("정상입니다.")
elif bmi <25:
    print("과체중입니다.")
else:
    print("비만입니다.")

