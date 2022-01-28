# Chapter 03-03
# Special Method (Masic Method) : Class 안에 정의할 수 있는 특별한(Built-in) 메소드 ['__()__' 형태]
# 파이썬의 핵심 -> 시퀀스(Sequence), 반복(Iterator), 함수(Functions), 클래스(Class)

# 객체 -> 파이썬의 데이터를 추상화
# 모든 객체 -> id, type -> value

# 일반적인 튜플
pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5) # 두 점을 나타내는 튜플 선언

from math import sqrt

l_leng1 = sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2) # 두 점 사이의 거리

print(l_leng1)

# 네임드 튜플 사용
from collections import namedtuple

# 네임드 튜플 선언 (네임드튜플 : 튜플인데 딕셔너리 형태 처럼 key와 value가 있는 튜플)
Point = namedtuple('Point', 'x y')

pt3 = Point(1.0, 5.0) # class 형식으로 tuple을 추상화하고 있다
pt4 = Point(2.5, 1.5)

# print(pt3)
# print(pt4) 자동으로 x y에 되는 것을 볼 수 있다. 이 개념은 데이터 모델에서 반드시 필요한 개념이다.

l_leng2 = sqrt((pt3.x - pt4.x) ** 2 + (pt3.y - pt4.y) ** 2) # 두 점 사이의 거리

print(l_leng2)

# 네임드 튜플 선언 방법
Point1 = namedtuple('Point', ['x', 'y']) # key 선언 시 리스트를 작성하여 선언가능
Point2 = namedtuple('Point', 'x,y') # 띄워쓰기 말고 이처럼 따옴표로 나누어도 된다.
Point3 = namedtuple('Point', 'x y') # 띄워쓰기로 선언한 경우
Point4 = namedtuple('Point', 'x y x class', rename = True) # 같은 key를 선언하거나(x) 예약어(class)를 key로 선언하지 못한다. 
# 하지만 rename = True 값으로 예외처리를 해주면 자동으로 난수 처리를 해주고 에러가 뜨지 않는다. if rename = False로 지정하면 선언자체에서 에러가 난다.

# 출력
print(Point1, Point2, Point3, Point4) # 네임드 튜플은 객체 상태로 맵핑되므로 class 형태로 나온다.

# Dict to Unpacking
temp_dict = {'x' : 75, 'y' : 55}

# 객체 생성
p1 = Point1(x=10, y=35) # 그냥 띄워쓰기를 해도 맵핑이 되지만 실수를 줄이기 위해 이렇게 작성도 가능하다.
p2 = Point(20, 40)
p3 = Point3(45, y=20)
p4 = Point4(10, 20, 30, 40)
p5 = Point3(**temp_dict) # dict 자료형으로 선언되어있는 temp_dict를 Unpacking(**)하여 Point3에 할당. Dict -> namedtuple

print(p1)
print(p2)
print(p3)
print(p4) # Point4에서 선언한 네임드 튜플에서 중복되거나 예약어들을 자동으로 _난수 형태로 선언하였다. -> 자주 쓰이지 않음.
print(p5)

# 사용
print(p1[0] + p2[1])
print(p1.x + p2.y) # 위에 보단 이처럼 명시적인 namedtuple을 사용하는 것이 좋다.

x, y = p3 # 이렇게도 Unpaking이 가능하다.
print(x, y)

# 네임드 튜플 메소드
temp = [52, 38]
p4 = Point1._make(temp) # .make() : List를 namedtuple로 변화시켜주는 메소드. 즉, 리스트로 새로운 객체를 생성해주는 메소드이다.
print(p4) # temp엔 인자가 2개여야만 한다. (할당하는 인자 수는 언제나 맞아야함)

print(p1._fields, p2._fields, p3._fields) # ._fields : key 값이 무엇이 있는지 출력해주는 메소드이다.

print(p1._asdict()) # _asdict() : OrderedDict 반환

# 실 사용 실습
# 반 20명, 4개의 반 (A,B,C,D)

Classes = namedtuple('Classes', ['rank', 'number']) # 각 반에서 20명의 번호를 가진 A10,D17 등 객체를 만드는 namedtuple 선언

# 그룹 리스트 선언
numbers = [str(n) for n in range(1,21)]
ranks = 'A B C D'.split()

print(numbers)
print(ranks)

# List comprehension
students = [Classes(rank, number) for rank in ranks for number in numbers]

print(len(students))
print(students)

# 추천
students2 = [Classes(rank, number) # 코드의 양을 줄이고 가독성을 높이는 방식으로 이처럼 작성도 가능하다. 위와 같은 코드이다.
            for rank in 'A B C D'.split()
                for number in [str(n)
                    for n in range(1,21)]]

print(len(students2))
print(students2)

# 출력
for s in students2:
    print(s)