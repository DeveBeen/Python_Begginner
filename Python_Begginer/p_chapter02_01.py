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

# 딕셔너리 구조
# 코드 반복 지속, 중첩 문제(키), 키 조회 예외 처리 등

car_dicts = [
    {'car_company': 'Ferrari', 'car_detail': {'color': 'White', 'horsepower': 400, 'price': 8000}},
    {'car_company': 'Bmw', 'car_detail': {'color': 'Black', 'horsepower': 270, 'price': 5000}},
    {'car_company': 'Audi', 'car_detail': {'color': 'Silver', 'horsepower': 300, 'price': 6000}}
]
# 삭제는 리스트와 비슷하게 pop과 del 메소드로 삭제 -> 결국 인덱스 번호를 알아야 함

# 클래스 구조
# 구조 설계 후 재사용성 증가, 코드 반복 최소화, 메소드 활용

class Car:
    def __init__(self, company, details):
        self._company = company
        self._details = details
    
    def __str__(self): # 매직 메소드 class 내부 객체를 출력 시 내가 원하는 형식으로 리턴해서 보여준 메소드이다. (원래 print를 쓰면 id값이 출력이 되지만 파이썬에 내장되어있는 __str__을 사용하면 원하는 형식으로 return이 가능하다.)
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self): # __srt__과 비슷한 메소드지만 __str__은 사용자를 위해 정보를 확인하는 방식의 메소드라면 __repr__은 객체에 엄격한 타입, 정보를 인식할 수 있는 공식적인 방식의 메소드
        return 'repr : {} - {}'.format(self._company, self._details)

car1 = Car('Ferrari', {'color': 'White', 'horsepower': 400, 'price': 8000})
car2 = Car('Bmw', {'color': 'Black', 'horsepower': 270, 'price': 5000})
car3 = Car('Audi', {'color': 'Silver', 'horsepower': 300, 'price': 6000})


print(car1) # __str__ 또는 __repr__ 메소드를 사용하여 원하는 형식으로 출력됨을 알 수 있다. (__str__ : 사용자, __repr__ : 개발자)
print(car2)
print(car3)

print(car1.__dict__) # .__dict__ 메소드 : 지정한 객체 안에 정보들을 볼 수 있다.
print(car2.__dict__)
print(car3.__dict__)

print(dir(car1)) # dir() : 지정한 객체 안에 있는 기능들을 나열하는 메타 정보 출력

# 리스트 선언
car_list = []

car_list.append(car1)
car_list.append(car2)
car_list.append(car3)

print(car_list) # 리스트안에 각각의 객체를 추가하여 출력 (여기서 중요한 점은 우리가 사용한 매직 메소드로 인해 출력된 모습 그대로 출력된다는 것)

for x in car_list:
    print(x) # 리스트 요소들을 for문으로 간단히 출력 가능하다.