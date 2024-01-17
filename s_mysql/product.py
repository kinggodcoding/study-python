from s_mysql.product_module import *

if __name__ == '__main__':
    # 상품 추가
    insert_query = "insert into tbl_product(name, price, created_date) \
                    values(%s, %s, %s)"

    insert_params = ['마우스', '85000', '2024-01-17T17:21:00']
    # save(insert_query, insert_params)

    # 전체 상품 조회
    find_all_query = "select id, name, price, created_date from tbl_product"
    products = find_all(find_all_query)

    for product in products:
        print(f'상품명: {product["name"]}')

    # 상품 정보 중 가격이 3000원 이상인 상품은 10% 할인해준다.
    update_query = "update tbl_product " \
                   "set price = price * 0.9 " \
                   "where price >= %s "
    update_params = ["3000"]
    update(update_query, update_params)

    # 평균 가격보다 높은 상품은 모두 삭제한다.
    delete_query = "delete from tbl_product " \
                   "where price >= avg(price) "
    delete_params = []
    delete(delete_query, delete_params)
