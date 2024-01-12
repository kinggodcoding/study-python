# email을 입력받고 아이디와 도메인을 각각 분리하여 출력한다.
id, domain = input('email 입력: ').split('@')
formatting = f'id: {id} 도메인: {domain}'
print(formatting)

'''
  첫 번째 값으로 야드를 입력받고, 두 번째 값으로 인치를 입력받아서
  각각 cm로 변환하여 다음 형식에 맞추어 소수점 둘 째자리까지 출력한다.
  round(값, 원하는 자리수) : 소수점이 맞춰진 결과값
    1yd: 91.44cm
    1in: 2.54cm

    예)
        yard 입력: 10
        inch 입력: 10

        10 yard는 914.4cm
        10 inch는 25.4cm
'''
yard, inch = map(float, input('yard inch 입력: ').split(', '))
yard_cm = round(yard * 91.44, 2)
inch_cm = round(inch * 2.54, 2)

formatting2 = f'{yard} yard는 {yard_cm}cm\n{inch} inch는 {inch_cm}cm'
print(formatting2)