'''
업 다운 게임
1 ~ 100의 범위 중 사용자에게 숫자를 입력받아 맞추는 게임
단 사용자가 exit를 입력하면 즉시 종료한다.
'''
# 랜덤하게 숫자를 섞기위한 랜덤 모듈 임포트
import random

# 1 ~ 100중 랜덤한 숫자 생성
random_number = random.randrange(1, 101)

msg = '1 ~ 100 중 숫자 한개를 입력하세요 : '

while True:
    user = input(msg)
    # 사용자가 exit를 입력하면 반복문 즉시 탈출
    if user == 'exit':
        print('게임 종료...')
    else:
        user_number = int(user)

    if user_number == random_number:
        print('정답입니다.')
        msg2 = '계속 하시겠습니까? Y/N : '
        y_or_n = input(msg2)
        if y_or_n == 'Y':
            random_number = random.randrange(1, 101)
            continue
        elif y_or_n == 'N':
            print('게임 종료...')
            break
    elif user_number > random_number:
        print(f'{user_number}보다 작습니다.')
    else:
        print(f'{user_number}보다 큽니다.')

