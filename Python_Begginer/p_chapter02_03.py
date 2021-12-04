# Chapter 02-03
# 객체지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지, 유지보수, 대형프로젝트
# 규모가 큰 프로젝트(프로그램) -> 함수 중심 -> 데이터 방대 -> 복잡
# 클래스 중심 -> 데이터 중심 -> 객체로 관리

class Car:
    """
    Car class
    Author : Kim
    Date : 2021.11.20
    Description : Class, Static, Instance Method
    """
 
    price_per_raise = 1.0

    def __init__(self, company, details):
        self._company = company
        self._details = details

    def __str__(self): 
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self): 
        return 'repr : {} - {}'.format(self._company, self._details)
    
    # Instance Method
    # Self : 객체의 고유한 속성값을 사용
    def detail_info(self): 
        print('Current ID : {}'.format(id(self)))
        print('Car Detail Info : {}, {}'.format(self._company, self._details.get('price')))

    # Instance Method
    def get_price(self): # 전 가격을 반환해주는 메소드 
        return 'Before Car Price -> company : {}, price : {}'.format(self._company, self._details.get('price'))

    # Instance Method
    def get_price_culc(self): # 후 가격을 반환해주는 메소드
        return 'After Car Price -> company : {}, price : {}'.format(self._company, self._details.get('price') * Car.price_per_raise)

    # Class Method : cls를 받는다.
    @classmethod # class 메소드는 @classmethod를 선언하면서 작성 시작
    def raise_price(cls, per): # class method의 각 인자는 self인 인스턴스가 아닌 cls라는 각 클래스를 받는다. 
        if per <= 1:
            print('Please Enter 1 Or More')
            return
        cls.price_per_raise = per # 이처럼 cls.(클래스변수) = (인자)를 선언한다.
        print('Succeed! price increased.')

    # Static Method : 아무것도 받지 않는다.
    @staticmethod # static 메소드는 @staticmethod를 선언하면서 작성 시작
    def is_bmw(inst):
        if inst._company == 'Bmw':
            return 'OK! This car is {}'.format(inst._company)
        return 'Sorry. This car is not Bmw.'

car1 = Car('Ferrari', {'color': 'White', 'horsepower': 400, 'price': 8000})
car2 = Car('Bmw', {'color': 'Black', 'horsepower': 270, 'price': 5000})

# 전체정보
car1.detail_info()
car2.detail_info()

# 가격정보 : 직접 접근 방식
print(car1._details.get('price')) # 이러한 인스턴스 변수 자체로 접근하는 방식은 좋은 방식이 아니다. -> 메소드로 만들어서 필요한 정보로 반환하는 방법을 많이 씀
print(car2._details['price']) # 이또한 직접 접근 방식으로 그리 좋은 방법은 아니다.

# 가격정보 : 클래스 접근 (매소드 사용)
print(car1.get_price())
print(car2.get_price())

# 가격 인상 (클래스 메소드 미사용)
Car.price_per_raise = 1.4 # class 메소드를 사용하지 않고 직접 접근한 방식이므로 그리 좋은 방식은 아니다.

# 가격 인상 후
print(car1.get_price_culc())
print(car2.get_price_culc())

# 클래스 메소드 사용 가격 인상 : 클래스 변수를 사용할 때는 클래스 메소드를 사용하여 핸들링 하는 것이 효율적이다.
Car.raise_price(1.6)

# 가격 인상 후
print(car1.get_price_culc())
print(car2.get_price_culc())

# 스태이틱 메소드 : 유연한 것이 특징
print(car1.is_bmw(car1))
print(car2.is_bmw(car2))
print(Car.is_bmw(car2)) # 클래스로 바로 호출도 가능하다.