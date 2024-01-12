# 추가, 수정, 삭제, 검색, 목록
# 수정 시 상품명으로 검색하고 새로운 상품명과 가격으로 수정한다(상품명 가격을 따로 수정하지 않고 한번에!)
# 검색 시 상품명, 가격을 따로 검색하도록 구현한다.
# 가격 검색 시 오차 범위는 ±50%로 설정한다.
name_list = []
price_list = []

title = ""
menu = "1.추가하기\n2.수정하기\n3.삭제하기\n4.검색하기\n5.목록보기\n6.나가기\n"
search_menu = "1.상품명으로 검색\n2.가격으로 검색\n"
append_message = '추가하실 상품명과 가격을 입력하세요.\n예)상품명 가격'
search_name_message_for_update = '수정하실 상품명을 입력하세요.'
update_message = '새로운 상품명과 가격을 입력하세요.\n예)상품명 가격'
delete_message = '삭제하실 상품명을 입력하세요.'
search_name_message, search_price_message = '상품명: ', '가격: '

append_error_message = "추가 실패(중복된 상품명)"
update_error_message = "수정 실패(존재하지 않는 상품명)"
delete_error_message = "삭제 실패(존재하지 않는 상품명)"
search_name_error_message = "검색 실패(존재하지 않는 상품명)"
search_error_message = "검색 결과가 없습니다."
error_message = "다시 입력해주세요."
no_item_message = "목록이 없습니다."

while True:

    user_select = int(input(menu))

    if user_select == 6:
        break

    elif user_select == 1:
        name, price = input(append_message).split(' ')
        if name in name_list:
            print(append_error_message)
            continue
        name_list.append(name)
        price_list.append(int(price))

    elif user_select == 2:
        user_search = input(search_name_message_for_update)
        if user_search in name_list:
            name, price = input(update_message).split(' ')
            price_list[name_list.index(name)] = int(price)
        else:
            print(update_error_message)
            continue

    elif user_select == 3:
        name = input(delete_message)
        if name in name_list:
            del price_list[name_list.index(name)]
            del name_list[name_list.index(name)]
        else:
            print(delete_error_message)
            continue

    elif user_select == 4:
        search_user_select = int(input(search_menu))
        if search_user_select == 1:
            name = input(search_name_message)
            if name in name_list:
                print(f'상품명 : {name}, 가격 : {price_list[name_list.index(name)]}')
            else:
                print(search_name_error_message)
                continue
        elif search_user_select == 2:
            price = int(input(search_price_message))
            S_price = price * 0.5
            B_price = price * 1.5
            print(f'입력한 가격은 : {price} +-50 오차범위 물품은 다음과 같습니다.')
            for i in price_list:
                if S_price <= i <= B_price:
                    print(f'{name_list[price_list.index(i)]}')

    elif user_select == 5:
        if len(name_list) == 0:
            print(no_item_message)
        for i in name_list:
            print(f'상품명 : {i} 가격 : {price_list[name_list.index(i)]}')


