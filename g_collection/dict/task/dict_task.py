# 추가, 수정, 삭제, 검색, 목록
# 수정 시 상품명으로 검색하고 새로운 상품명과 가격으로 수정한다(상품명 가격을 따로 수정하지 않고 한번에!)
# 검색 시 상품명, 가격을 따로 검색하도록 구현한다.
# 가격 검색 시 오차 범위는 ±50%로 설정한다.
data_dict = {}

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
        if new_name not in data_dict:
            # 입력받은 상품명과 가격을 딕셔너리에 추가
            data_dict[new_name] =int(new_price)
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
        # 수정할 상품명이 상품명 딕셔너리 키값에 있다면
        if name in data_dict:
            # 새로운 상품명과 가격을 구분점은 공백으로 입력받아 new_name, new_price 변수에 저장
            new_name, new_price = input(update_message).split()
            # 새롭게 입력받은 상품명이 딕셔너리에 들어가 있지 않으면
            if new_name not in data_dict:
                # 딕셔너리의 원래 상품명이 있던 키값에 새로운 가격을 넣어주면 됨
                del data_dict[name]
                data_dict[new_name] = int(new_price)
                continue
            else:
                result_message = update_error_message2
        # 수정할 상품명이 딕셔너리에 없다면
        else:
            # 애초에 목록에도 들어가있지 않음 따라서 수정할 수 없음 -> 에러 메세지 출력(일괄 처리)
            result_message = update_error_message1

    # 삭제
    elif choice == 3:
        # 삭제할 상품명을 사용자에게 입력받음
        name = input(delete_message)
        # 입력받은 삭제할 상품명이 딕셔너리에 있다면
        if name in data_dict:
            # 삭제할 상품명을 딕셔너리에서 삭제 시켜주면 됨
            del data_dict[name]
            continue
        # 입력받은 상품명이 딕셔너리 없다면 삭제할 수 없으므로 에러 메시지를 result_message에 담아 밑에 일괄처리
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
            # 검색할 상품명이 딕셔너리에 있다면
            if name in data_dict:
                # 딕셔너리의 키값과 그에 해당하는 벨류값을 출력
                print(f'{name}, {data_dict[name]}')
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
            result_list = []
            for key, value in data_dict.items():
                if min <= value <= max:
                    result_list.append((key, value))

            # 위의 오차범위를 통해 만들어 낸 인덱스의 길이가 0이 아니라면 즉 비어있지 않다면
            if len(result_list) != 0:
                # 오차범위안의 딕셔너리에서 하나씩 뽑아 상품명과 가격을 출력
                for i in result_list:
                    print(f'{i}')
                    continue
            # 만약 오차범위 내 딕셔너리가 비어있다면 에러메시지 일괄 처리
            else:
                result_message = search_error_message
    # 목록
    elif choice == 5:
        # 상품명 딕셔너리가 비어있다면 목록이 없다는 말과 같음
        if len(data_dict) == 0:
            # 따라서 에러메시지 일괄 처리
            result_message = no_item_message
        # 비어 있지 않다면
        else:
            # 딕셔너리의 키와 값을 한번에 가져와서 출력
            for key, value in data_dict.items():
                print(f'{key}, {value}')
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
