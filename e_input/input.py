# 문자열끼리만 연결(+)이 가능하다!
# data = 3
# print('안' + str(data))

# name = input("이름: ")
# print(f'{name}님 환영합니다.')

# 제 이름은 ???, 키는 ???cm입니다.
# name = input("이름: ")
# height = input("키: ")
# formatting = f'제 이름은 {name}, 키는 {height}cm입니다.'
# print(formatting)

# 두 정수를 입력받은 후 곱셈 결과 출력
# number1 = int(input("첫 번째 정수 입력: "))
# number2 = int(input("두 번째 정수 입력: "))
# result = number1 * number2
# formatting1 = f'{number1} x {number2} = {result}'
# print(formatting1)

# map(각각 어떻게 바꿀 것인가, [])
# message = '두 정수를 입력하세요.'
# example_message = '예)1, 3'
# number1, number2 = map(int, input(message + '\n' + example_message).split(', '))
# result = number1 * number2
# formatting = f'{number1} * {number2} = {result}'
# print(formatting)

# 현재 시간을 입력하고 시와 분리하여 출력
time, minutes = map(int, input("현재 시간을 입력하세요\n 예) 3:45\n").split(':'))
formatting = f'현재 시간은 {time}시 {minutes}분 입니다.'
print(formatting)

# 핸드폰 번호를 -(하이폰)과 함께 입력받은 뒤 각 자리의 번호를 분리해서 출력
phone_number1, phone_number2, phone_number3 = input('핸드폰 번호를 입력하세요.\n 예) 000-0000-0000 \n').split('-')
formatting2 = f'앞자리: {phone_number1} 가운데자리: {phone_number2} 마지막자리: {phone_number3}'
print(formatting2)

# 이름과 니이를 한 번에 입력받은 뒤 "000님의 나이는 000살" 형식으로 출력
name, age = input('이름과 나이를 한번에 입력하세요\n 예) 김수빈, 26\n').split(', ')
formatting3 = f'이름: {name}  나이: {age}살'
print(formatting3)

# 3개의 정수를 입력받은 뒤 덧셈 결과 출력
num1, num2, num3 = map(int, input("세개의 정수를 입력\n").split(', '))
sum = num1 + num2 + num3
formatting4 = f'{num1} + {num2} + {num3} = {sum}'
print(formatting4)