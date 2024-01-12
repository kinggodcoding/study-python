# user_info = [
#     {'number': 1, 'name': 'john'},
#     {'number': 2, 'name': 'mike'},
#     {'number': 3, 'name': 'ted'},
#     {'number': 4, 'name': 'lindy'},
#     {'number': 5, 'name': 'adam'},
# ]
#
#
# # 추가
# # def insert(*, number, name):
# #     '''
# #
# #     :param number: 회원 번호
# #     :param name: 회원 이름
# #     '''
# #     user_info.append({'number': number, 'name': name})
#
# # 추가
# # 회원 번호는 자동 증가한다.
# def insert(*, name):
#     '''
#
#     :param number: 회원 번호
#     :param name: 회원 이름
#     '''
#
#     for i in range(len(user_info)):
#         if i + 1 == len(user_info):
#             number = i + 2
#             user_info.append({'number': number, 'name': name})
#
# # 목록
# def menu():
#     for i in user_info:
#         menu = f'번호 :{i["number"]} 이름 :{i["name"]}'
#         return menu
#
# # 조회(번호로 조회)
# def search(*, number):
#     for i in user_info:
#         if i['number'] == number:
#             search = f'번호 {number}번은 {i["name"]}입니다'
#             return search
#
#
# # 수정(번호로 이름 수정)
# def update(*, number, name):
#     for i in user_info:
#         if i['number'] == number:
#             i['name'] = name
#
#
# # 삭제(번호로 삭제)
# def delete(*, number):
#     for i in user_info:
#         if i['number'] == number:
#             index = user_info.index(i)
#             del user_info[index]
#
#
#
# delete(number=3)
# print(user_info)

post_info = [
    {'number': 1, 'title': '테스트 제목1', 'content': '테스트 내용1', 'file': '/usr/post/file/img001.png', 'read_count': 0},
    {'number': 2, 'title': '테스트 제목2', 'content': '테스트 내용2', 'file': '/usr/post/file/img002.png', 'read_count': 0},
    {'number': 3, 'title': '테스트 제목3', 'content': '테스트 내용3', 'file': '/usr/post/file/img003.png', 'read_count': 0},
    {'number': 4, 'title': '테스트 제목4', 'content': '테스트 내용4', 'file': '/usr/post/file/img004.png', 'read_count': 0},
    {'number': 5, 'title': '테스트 제목5', 'content': '테스트 내용5', 'file': '/usr/post/file/img005.png', 'read_count': 0}
]

# 추가(조회수는 전달받지 않고 기본값 0으로 설정)
number = 5
def insert(*, title, content, file, read_count= 0):
    '''

    :param title: 테스트 제목
    :param content: 테스트 내용
    :param file: 파일명
    :param read_count: 조회수
    '''
    global number
    number += 1
    post_info.append({'number': number, 'title': title, 'content': content, 'file': file, 'read_count': read_count})

# insert(title= '테스트 제목6', content= '테스트 내용6', file= '/usr/post/file/img006.png')
# print(post_info)

# 목록(최신순으로 조회)
def select_all():
    return post_info[::-1]

# 조회(번호로 조회, 조회수 1 증가)
def select(num):
    '''

    :param num: 번호
    :return:
    '''
    for post in post_info:
        if post['number'] == num:
            post['read_count'] += 1
            return post

# 수정(번호로 정보 수정)
def update(**kwargs):
    for post in post_info:
        if post['number'] == kwargs['number']:
            post['title'] = kwargs['title']
            post['content'] = kwargs['content']
            post['file'] = kwargs['file']
            return post

# 삭제(번호로 삭제)
def delete(number):
    del post_info[post_info.index(select(number))]

select(1)
select(2)
select(1)

print(post_info)