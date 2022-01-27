# Chapter 03-01 : 파이썬 데이터 모델
# Special Method (Masic Method) : Class 안에 정의할 수 있는 특별한(Built-in) 메소드 ['__()__' 형태]
# 파이썬의 핵심 -> 시퀀스(Sequence), 반복(Iterator), 함수(Functions), 클래스(Class)

# 기본형
print(int) # 이를 출력하면 <class 'int'> 가 출력됨을 볼 수 있는데 이는 우리가 써왔던 모든 자료형이 class로 이루어짐을 말해준다.
print(float)

# 모든 속성
print(dir(int))
print(dir(float))

n = 10

print(n + 100) # 이는 내부적으로 Built-in 되어있는 __add__ Method가 실행된 것이다.
print(n.__add__(100)) # 이처럼 메소드 자체를 사용하여 위와 같은 결과값을 가져올 수 있다.
print(n.__doc__) # 이처럼 내부적으로 선언된 class int에 대한 주석을 __doc__ 메소드로 확인 할 수 있다.
print(n.__bool__(), bool(n)) # 이처럼 직접적으로 메소드를 호출하여, 또는 이미 맵핑되어 있는 bool() 함수를 사용하여 같은값을 도출할 수 있다.
print(n * 100, n.__mul__(100))

# Class 예제 1
class Fruit:
    def __init__(self, name, price): # 생성자 메소드
        self._name = name # 인스턴스 변수
        self._price = price

    def __str__(self): # 객체 정보를 보기 편한 __str__ 메소드
        return 'Fruit Class Info : {} {}'.format(self._name, self._price)
    
    def __add__(self, x): # 더하기 메소드로 간단한 + 코드로 알아서 가격을 더해서 줄력해주는 메소드이다.
        print('Called >> __add__')
        return self._price + x._price

    def __sub__(self, x): # 뺴기 메소드로 더하기와 같은 원리로 작동되는 메소드이다.
        print('Called >> __sub__')
        return self._price - x._price
    
    def __le__(self, x): # 크기 비교 메소드이다.
        print('Called > __le__')
        if self._price <= x._price:
            return True
        else:
            return False

    def __ge__(self, x): # 크기 비교 메소드이다. (__le__ 메소드랑 상반되는 개념이다.)
        print('Called > __ge__')
        if self._price >= x._price:
            return True
        else:
            return False

# 인스턴스 생성
s1 = Fruit('Orange', 7500)
s2 = Fruit('Banana', 3000)

# print(s1._price + s2._price) -> 일반적인 계산 방식 : 코드길이가 길고 복잡한 단점이 존재한다.
print(s1 + s2) # add 메소드를 구현하였으므로, 과일 + 과일이라는 형태를 받아 가격을 더해주는 형식으로 출력이 가능하다.

# 매직메소드
print(s1 >= s2) # ge 메소드 실행 
print(s1 <= s2) # le 메소드 실행
print(s1 - s2) # sub 메소드 실행
print(s2 - s1) # sub 메소드 실행
print(s1)
print(s2) # str 메소드 실행
