'''
if문을 이용한 동물 맞추기 게임
동물원에 토끼, 강아지, 고양이, 호랑이, 코끼리 다섯마리의 동물이 있다.
동물 한 마리를 선택하여 랜덤하게 나오는 동물과 맞추면 되는 게임이다.
'''
# 동물을 랜덤하게 뽑기 위한 랜덤 모듈
import random
# 동물들을 리스트에 담기
zoo = ['토끼', '강아지', '고양이', '호랑이', '코끼리']
# 담은 동물 들 중 한마리를 랜덤하게 뽑기
animal = random.choice(zoo)

# 사용자에게 동물 입력받기
message = '동물을 입력해주세요 : '
user_choice_animal = input(message)
result = ''
if user_choice_animal == animal:
    result = f'동물은 : {animal} 당신이 입력한 동물은 {user_choice_animal}\n 정답입니다.'
else:
    result = f'동물은 : {animal} 당신이 입력한 동물은 {user_choice_animal}\n 오답입니다.'

print(result)
