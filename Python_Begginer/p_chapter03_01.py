# Chapter 03-01
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


