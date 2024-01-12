# # animals = ["dog", "cat", "bird", "fish"]
# # print(animals)
# # print(type(animals))
# #
# # # 인덱스로 접근
# # print(animals[1])
# # print(animals[2])
# #
# # # 음수 인덱스 가능(가장 마지막부터 순서대로 앞으로 이동한다)
# # print(animals[-1])
# # print(animals[-2])
# #
# # # len()
# # print(len(animals))
# #
# # # append()
# # animals.append("hamster")
# # print(len(animals))
# # print(animals)
# #
# # animals.append("cat")
# # print(animals)
# #
# # # insert()
# # animals.insert(1, "dog")
# # print(animals)
# #
# # # remove()
# # animals.remove('fish')
# # print(animals)
# #
# # # del()
# # # del(animals[1])
# # del animals[1]
# # print(animals)
# #
# # # clear()
# # # animals.clear()
# # # print(animals)
# #
# # # index()
# # print(animals.index('bird'))
# # # print(animals.index('tiger'))
# #
# # # 수정
# # index = animals.index('bird')
# # animals[index] = "lion"
# # print(animals)
# #
# # # 그 외
# # animals = ["dog", "cat", "bird", "fish"]
# # print(animals * 2)
# #
# # print("dog" in animals)
# # print("tiger" in animals)
# #
# # for animal in animals:
# #     print(animal)
#
# # 실습
# # 1~90까지 list에 담고 출력
# num_list = []
# for i in range(90):
#     num_list.append(i + 1)
# print(num_list)
#
# # 1~100까지 중 짝수만 list에 담고 출력
# num_list2 = []
# for i in range(100):
#     if (i + 1) % 2 == 0:
#         num_list2.append(i + 1)
# print(num_list2)
#
# # 1~10까지 list에 담은 후 짝수만 출력
# num_list3 = []
# for i in range(10):
#     num_list3.append(i + 1)
# # even_list = [0] * (len(num_list3) / 2)
# even_list = []
# for i in range(len(num_list3)):
#     if num_list3[i] % 2 == 0:
#         even_list.append(num_list3[i])
# print(even_list)
# # print(num_list3)
#
# # 4명의 회원 정보를 list에 담은 뒤 두번 째 회원의 이름을 변경하고 마지막 회원은 삭제
# user_list = ['김수빈', '홍길동', '아무개', '000']
# index = user_list.index('홍길동')
# user_list[index] = '변경된홍길동'
# real_money = ''
#
# del user_list[-1]
# print(user_list)
#
# # "189,000 원"을 189000으로 변경, 제네레이터 사용
# string_money = "189,000 원"
# money_list = []
# for i in string_money:
#     if i == ',' or i == ' ' or i == '원':
#         continue
#     else:
#         money_list.append(i)
#
# for i in money_list:
#     real_money += i
#
# real_money2 = int(real_money)
# print(real_money2)

# list안에 list
number_list = [[1, 3, 5], [2, 4, 6]]
# print(number_list[0][0])
for i in range(len(number_list)):
    for j in range(len(number_list[i])):
        print(number_list[i][j])