# Chapter04-02
# 파이썬의 모든 자료형은 두 개의 형식으로 나눌 수 있다.
# 시퀀스형
# 컨테이너(Container : 서로 다른 자료형 [List, tuple, collections.deque 등]을 담을 수 있는 형태)
# 플랫(Flat : 한개의 자료형 [str, bytes, bytearray, array.array, memoryview 등]을 담을 수 있는 형태) -> 한개의 자료형만을 담을 수 있지만 그 만큼 빠르고 정확하다.
# 가변형(List, bytearray, array.array, memoryview, deque 등) -> 데이터 갑을 입력 후에 변경이 가능한 자료형 
# 불변형(tuple, str, bytes 등) -> 입력된 데이터 값을 변경 할 수 없는 자료형이다.

# Tuple Advanced
# Unpackiing

# b, a = a, b

print(divmod(100, 9)) # divmod(a, b) : a를 b로 나누었을 때, 몫과 나머지를 출력해주는 함수
print(divmod(*(100, 9))) # Tuple로 받고 싶으면 언패킹 기호 * (아스타) 를 앞에 붙여 할당해야 한다.
print(*(divmod(100, 9))) # Unpacking을 통하여 결과 값을 출력도 가능하다.

x, y, *rest = range(10) # 변수에 너무 많은 값을 넣으려 해서 오류가 생긴다. 하지만 이처럼 unpack을 해주면 값이 리스트 값으로 들어간다.
print(x, y, rest)
x, y, *rest = range(2)
print(x, y, rest)
x, y, *rest = 1, 2, 3, 4, 5
print(x, y, rest)