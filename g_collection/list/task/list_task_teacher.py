# 추가, 수정, 삭제, 검색, 목록
# 수정 시 상품명으로 검색하고 새로운 상품명과 가격으로 수정한다(상품명 가격을 따로 수정하지 않고 한번에!)
# 검색 시 상품명, 가격을 따로 검색하도록 구현한다.
# 가격 검색 시 오차 범위는 ±50%로 설정한다.
name_list = []
price_list = []

title = "또와 과일"
menu = "1.추가하기\n2.수정하기\n3.삭제하기\n4.검색하기\n5.목록보기\n6.나가기\n"
search_menu = "1.상품명으로 검색\n2.가격으로 검색\n"
append_message = '추가하실 상품명과 가격을 입력하세요.\n예)상품명 가격'
search_name_message_for_update = '수정하실 상품명을 입력하세요.'
update_message = '새로운 상품명과 가격을 입력하세요.\n예)상품명 가격'
delete_message = '삭제하실 상품명을 입력하세요.'
search_name_message, search_price_message = '상품명: ', '가격: '

result_message = ""
append_error_message = "추가 실패(중복된 상품명)"
update_error_message1 = "수정 실패(존재하지 않는 상품명)"
update_error_message2 = "수정 실패(중복된 상품명)"
delete_error_message = "삭제 실패(존재하지 않는 상품명)"
search_name_error_message = "검색 실패(존재하지 않는 상품명)"
search_error_message = "검색 결과가 없습니다."
error_message = "다시 입력해주세요."
no_item_message = "목록이 없습니다."

while True:
    # 사용자에게 메뉴를 보여주고 선택한 번호를 choice에 저장
    choice = int(input(title + '\n' + menu))

    # 추가
    if choice == 1:
        # 사용자에게 상품명과 가격을 동시에 입력받는다(구분점은 공백문자).
        new_name, new_price = input(append_message).split()
        # 입력한 상품명이 기존 상품과 중복되지 없다면,
        if new_name not in name_list:
            # 이름 list에 추가
            name_list.append(new_name)
            # 가격 list에 추가
            price_list.append(int(new_price))
            # 오류 메세지를 출력하지 않기 위해서 즉시 다음 반복으로 skip
            continue
        else:
            # 입력한 상품명이 기존 상품과 중복되었다면,
            # 알맞은 메세지를 result_message에 담아서 소스코드 하단의 일괄처리로 보내기
            result_message = append_error_message

    # 수정
    elif choice == 2:
        # 사용자에게 수정할 상품명을 입력받아 name에 저장
        name = input(search_name_message_for_update)
        # 수정할 상품명이 상품명 리스트에 있다면
        if name in name_list:
            # 새로운 상품명과 가격을 구분점은 공백으로 입력받아 new_name, new_price 변수에 저장
            new_name, new_price = input(update_message).split()
            # 새롭게 입력받은 상품명이 상품명 리스트에 들어가 있지 않으면
            if new_name not in name_list:
                # 상품명 리스트의 원래 수정할 상품명이 있던 인덱스를 찾고
                index = name_list.index(name)
                # 상품명 리스트의 원래 상품명이 있던 자리, 가격 리스트의 원래 상품의 가격이 있던 자리에 수정할 상품명, 수정할 가격을 넣어줌
                name_list[index], price_list[index] = new_name, new_price
                continue
            else:
                result_message = update_error_message2
        # 수정할 상품명이 상품명 리스트에 없다면
        else:
            # 애초에 목록에도 들어가있지 않음 따라서 수정할 수 없음 -> 에러 메세지 출력(일괄 처리)
            result_message = update_error_message1

    # 삭제
    elif choice == 3:
        # 삭제할 상품명을 사용자에게 입력받음
        name = input(delete_message)
        # 입력받은 삭제할 상품명이 상품명 리스트에 있다면
        if name in name_list:
            # 상품명 리스트의 삭제할 상품명의 인덱스 즉 위치를 찾고
            index = name_list.index(name)
            # 상품명 리스트와 가격 리스트의 삭제할 상품이 있는 위치의 인덱스를 넣어서 del 명령어를 사용해 삭제 시킴
            del name_list[index]
            del price_list[index]
            continue
        # 입력받은 상품명이 상품명 리스트에 없다면 삭제할 수 없으므로 에러 메시지를 result_message에 담아 밑에 일괄처리
        else:
            result_message = delete_error_message

    # 검색
    elif choice == 4:
        # 상품명으로 검색할지, 가격으로 검색할지를 입력받아 저장
        choice = int(input(search_menu))

        # 상품명으로 검색
        if choice == 1:
            # 검색할 상품명을 입력받고
            name = input(search_name_message)
            # 검색할 상품명이 상품명 리스트에 있다면
            if name in name_list:
                # 상품명 리스트의 검색할 상품명의 인덱스를 저장하여
                index = name_list.index(name)
                # 상품명 리스트의 검색할 상품명의 인덱스 가격 리스트의 검색할 상품명의 인덱스를 통해 상품명과 가격을 출력
                print(f'{name_list[index]}, {price_list[index]}')
                continue
            # 검색할 상품명이 상품명 리스트에 없다면 검색할 수 없으므로 에러 메시지를 일괄 처리
            else:
                result_message = search_name_error_message

        # 가격으로 검색
        elif choice == 2:
            # 가격을 입력받아 int로 형변환 한후
            price = int(input(search_price_message))
            # 오차범위 +- 50이니 0.5, 1.5를 원래 가격에 곱해준 후
            min = price * 0.5
            max = price * 1.5
            # 리스트 컴프리헨션을 통해
            # 오차범위 내에 있는 가격의 상품명을 리스트에 담음
            result_index = [price_list.index(i) for i in [price for price in price_list if min <= price <= max]]

            # 위의 오차범위를 통해 만들어 낸 인덱스의 길이가 0이 아니라면 즉 비어있지 않다면
            if len(result_index) != 0:
                # 오차범위 내 리스트를 하나씩 뽑아 상품명과 가격을 출력
                for i in result_index:
                    print(f'{name_list[i]}, {price_list[i]}')
                    continue
            # 만약 오차범위 내 리스트가 비어있다면 에러메시지 일괄 처리
            else:
                result_message = search_error_message
    # 목록
    elif choice == 5:
        # 상품명 리스트가 비어있다면 목록이 없다는 말과 같음
        if len(name_list) == 0:
            # 따라서 에러메시지 일괄 처리
            result_message = no_item_message
        # 비어 있지 않다면
        else:
            # 상품명 리스트의 길이 만큼 반복문을 돌려 모든 상품명, 가격을 출력 -> 즉 첫번째 상품, 첫번째 상품의 가격 이렇게 될 것임
            for i in range(len(name_list)):
                print(f'{name_list[i]}, {price_list[i]}')
                continue

    # 나가기
    # 만약에 사용자가 6을 입력하였으면 즉시 반복문을 탈출해야 함 따라서 break를 통해 즉시 탈출
    elif choice == 6:
        break

    # 그 외
    # 만약 사용자가 1 ~ 6번이외의 문자나 번호를 선택하였으면 항목에 없는 것을 선택하였으므로 에러 메시지 일괄 처리
    else:
        result_message = error_message

    # 에러 메시지 출력(일괄 처리)
    print(result_message)
    # 출력 후 result_message는 비워져있어야함 만약 비우지않는다면 전에 출력했던 에러 메시지가 계속 붙여서 나올 것임
    result_message = ""
