# Chapter 02-01
# 객체지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지, 유지보수, 대형프로젝트
# 규모가 큰 프로젝트(프로그램) -> 함수 중심 -> 데이터 방대 -> 복잡
# 클래스 중심 -> 데이터 중심 -> 객체로 관리

class Car:
    """ 해당 클래스를 소개하는 주석
    Car class
    Author : Kim
    Date : 2021.11.20
    """
    # 클래스 변수 : 모든 인스턴스가 공유하지만, 인스턴스 변수 자체 값에는 영향을 주지 않는다.
    car_count = 0

    def __init__(self, company, details):
        self._company = company
        self._details = details
        # self.car_count = 10 -> 클래스 변수로 car_count가 존재해도 인스턴스 변수로 따로 정의 할 수 있다. 이는 인스턴스 변수 내 값으로 저장된다.
        Car.car_count += 1 # 인스턴스 변수가 1개 씩 추가 될 때마다 1씩 증가
    
    def __del__(self):
        Car.car_count -= 1

    def __str__(self): 
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self): 
        return 'repr : {} - {}'.format(self._company, self._details)

    def detail_info(self): # 이처럼 클래스내에 나의 메소드를 만들 수 있다.
        print('Current ID : {}'.format(id(self)))
        print('Car Detail Info : {}, {}'.format(self._company, self._details.get('price')))


# self 의미 : 인스턴스 메소드
car1 = Car('Ferrari', {'color': 'White', 'horsepower': 400, 'price': 8000})
car2 = Car('Bmw', {'color': 'Black', 'horsepower': 270, 'price': 5000})
car3 = Car('Audi', {'color': 'Silver', 'horsepower': 300, 'price': 6000})

# ID 확인 : 출력값을 보면 각각의 다른 ID(고유번호)를 가지고 있으므로 나만의 것(self)가 붙는다.
print(id(car1))
print(id(car2))
print(id(car3))

print(car1._company == car2._company) # == 기호는 값을 비교한 거지만
print(car1 is car2) # is 는 인스턴스 자체를 비교한 것이다.

# dir & __dict__ 확인
print(dir(car1))
print(dir(car2)) # dir은 상속받는 모든 속성을 출력해주고 (리스트형으로)

print(car1.__dict__)
print(car2.__dict__) # __dict__는 네임스페이스인 값을 보고 싶을 떄 사용 (딕셔너리형)

# Doctring
print(Car.__doc__) # __doc__는 내가 만든 클래스에 단 주석을 출력해준다. (협업할 떄, 많이 사용)

# 내가 만든 class 메소드 실행
car1.detail_info() # 이렇게 내가 만든 메소드에 인스턴스를 할당하여 활용할 수 있다.
car2.detail_info()
car3.detail_info()

# 비교
print(car1.__class__, car2.__class__) # __class__는 부모 클래스를 출력해준다.
print(id(car1.__class__), id(car2.__class__))  # __class__로 가져온 부모는 결국 다 동일한 Car class이므로 id값은 어떤 인스턴스 변수든 동일하다.

# 에러 : 클래스 자체를 사용할 떄는 항상 할당을 해줘야 에러가 나지 않는다. 
Car.detail_info(car1) # 아래와 같이 인스턴스 변수에 detail_info 메소드를 실행 할 수 있지만, 클래스 자체를 사용하여 이처럼 실행할 수도 있다.
car1.detail_info() # 이는 전방에 이미 self인자인 인스턴스 변수를 할당한 후 메소드를 실행한 경우기 때문에 에러가 딱히 나지 않는다. 위에 같은 경우는 클래스 자체로 접근했기 때문에 ()안에 인스턴스 변수(self)를 할당해줘야 한다.

print(car1.car_count) # car1 - car3까지 3개를 할당하였으므로, 모든 인스턴스 변수에 대한 car_count 값은 3이다.

print(dir(car1)) # 속성과, 메소드가 뜨던 dir 정보에서 class 변수가 추가 되있음을 볼 수 있다.

# 접근 : 접근은 인스턴스 부모로 하든 클래스 자체로 하든 가능하다.
print(car1.car_count) # 만약 __init__ 메소드에 car_count 라는 동일한 이름의 인스턴스 변수가 있을 시 이 경우는 car1 이라는 인스턴스에 접근한 car_count 이므로 인스턴스 변수 self.car_count가 출력되지만
print(Car.car_count) # 이는 부모 클래스에서 car_count로 접근했으므로 인스턴스 변수들이 공유하는 클래스 변수 car_count가 출력이 된다. (83-85 주석 참고)

# 삭제 확인
del car2
print(Car.car_count) # __del__ 메소드로 인스턴스의 삭제를 클래스 변수로 공유할 수 있다.

# 인스턴스 네임스페이스에 없으면 상위에서 검색
# 즉, 동일한 이름으로 변수 생성 가능 (인스턴스 검색 후 -> 상위 (클래스 변수, 부모 클래스))
# 만약 class 변수 중에 car_count가 존재하고 __init__ 메소드 내에 self.car_count 라는 인스턴스 변수가 있을 수 있다는 뜻