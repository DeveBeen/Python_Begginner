# Chapter 03-02
# Special Method (Masic Method) : Class 안에 정의할 수 있는 특별한(Built-in) 메소드 ['__()__' 형태]
# 파이썬의 핵심 -> 시퀀스(Sequence), 반복(Iterator), 함수(Functions), 클래스(Class)

# 클래스 예제 2
# Vector의 계산
# add : (5,2) + (4,3) = (9,5)
# mul : (10,3) * 5 = (50,15)
# Max : (5,10) = 10

class Vector(object):
    '''dsdsds'''

    def __init__(self, *args): # unpacking으로 받는 __init__
        '''Create a vector, example : v = Vector(5, 10)''' # 이처럼 메소드 단위로 주석을 달아 호출할 수 있다.
        if len(args) == 0: # 오류를 사전에 예방하기 위해 언제나 예외 처리를 해야한다.
            self._x, self._y = 0, 0 # 만약 Vector()이라 선언했을 시에 각각 0으로 언패킹
        else:
            self._x, self._y = args # 일반 언패킹

    def __repr__(self):
        '''Return the vector informations.'''
        return 'Vector(%r, %r)' % (self._x, self._y)

    def __add__(self, other):
        '''Return the vector addtion of self and other'''
        return Vector(self._x + other._x, self._y + other._y)

    def __mul__(self, y):
        return Vector(self._x * y, self._y * y)

    def __bool__(self):
        return bool(max(self._x, self._y)) # 0,0 인지를 확인 하는 메소드 -> 최댓값이 0 이면 둘 다 0

# Vector 인스턴스 생성
v1 = Vector(5,7)
v2 = Vector(23, 35)
v3 = Vector()

# 매직메소드 출력
print(Vector.__init__.__doc__) # 이처럼 메소드 자체 주석이 아닌 __init__ 메소드의 주석을 호출 가능하다.
print(Vector.__repr__.__doc__)
print(Vector.__add__.__doc__)
print(v1, v2, v3)
print(v1 + v2)
print(v1 * 3)
print(v2 * 10)
print(bool(v1), bool(v2), bool(v3))