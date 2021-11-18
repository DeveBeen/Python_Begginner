# Chapter 02-01
# 객체지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지, 유지보수, 대형프로젝트
# 규모가 큰 프로젝트(프로그램) -> 함수 중심 -> 데이터 방대 -> 복잡
# 클래스 중심 -> 데이터 중심 -> 객체로 관리

# 일반적인 코딩 -> 아래 차량 1,2,3의 예시 처럼 복사 붙여넣기 방식으로 데이터를 쭉 나열하게 되면 코드가 길어지고 데이터가 커지므로, 코드의 방향성이 객체지향으로 변화하기 시작했다.

# 차량 1
car_company_1 = 'Ferrari'
car_detail_1 = [
    {'color': 'White'},
    {'horsepower': 400},
    {'price': 8000}
]

# 차량 2
car_company_2 = 'Bmw'
car_detail_2 = [
    {'color': 'Black'},
    {'horsepower': 270},
    {'price': 5000}
]

# 차량 3 -> 자동차의 종류와 가격 변동 등 추가, 수정이 힘든 방식이다.
car_company_3 = 'Audi'
car_detail_3 = [
    {'color': 'Silver'},
    {'horsepower': 300},
    {'price': 6000}
]

# 리스트 구조 : 관리하기가 불편하고, 인덱스 접근 시 실수 가능성이 높고, 삭제가 불편하다. (데이터가 많아지면 인덱스 번호를 알아야 하므로 비효율적이다.)
car_company_list = ['Ferrari', 'Bmw', 'Audi']
car_detail_list = [
    {'color': 'White', 'horsepower': 400, 'price': 8000},
    {'color': 'Black', 'horsepower': 270, 'price': 5000},
    {'color': 'Silver', 'horsepower': 300, 'price': 6000}
]

del car_company_list[1] # 이처럼 인덱스 번호를 알아야 하므로 데이터가 많아 질수록 삭제가 번거롭다.
del car_detail_list[1]

print(car_company_list)
print(car_detail_list)

