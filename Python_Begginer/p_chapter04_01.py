# Chapter04-01
# 파이썬의 모든 자료형은 두 개의 형식으로 나눌 수 있다.
# 시퀀스형
# 컨테이너(Container : 서로 다른 자료형 [List, tuple, collections.deque 등]을 담을 수 있는 형태)
# 플랫(Flat : 한개의 자료형 [str, bytes, bytearray, array.array, memoryview 등]을 담을 수 있는 형태) -> 한개의 자료형만을 담을 수 있지만 그 만큼 빠르고 정확하다.
# 가변형(List, bytearray, array.array, memoryview, deque 등) -> 데이터 갑을 입력 후에 변경이 가능한 자료형 
# 불변형(tuple, str, bytes 등) -> 입력된 데이터 값을 변경 할 수 없는 자료형이다.

# 리스트 및 튜플 고급
# 지능형 리스트(Comprehending Lists)
chars = '+_)(*&^%$#@!)' # str형으로 Flat형으고 불변형이다
code_list1 = []

for s in chars:
    # 유니코드 리스트
    code_list1.append(ord(s)) # str형은 시퀀스의 형식이므로 리스트형으로 만들 수 있다.


print(code_list1)

# Comprehending Lists
code_list2 = [ord(s) for s in chars] # 이와같은 형태가 위에 보다 조금 더 효율적고 빠르다.

print(code_list2)

# Comprehending Lists + Map, Filter
code_list3 = [ord(s) for s in chars if ord(s) > 40] # 이처럼 지능형 리스트에는 조건도 추가가 가능하다.
code_list4 = list(filter(lambda x : x > 40, map(ord, chars))) # 이처럼 map과 filter을 사용하여 같은 결과를 도출 할 수 있다.

print(code_list3)
print(code_list4)

# 전체 출력
print(code_list1)
print(code_list2)
print(code_list3)
print(code_list4)
print([chr(s) for s in code_list1]) # ord -> 유니코드 변형 -> chr -> 문자로 다시 변형
print([chr(s) for s in code_list2])
print([chr(s) for s in code_list3])
print([chr(s) for s in code_list4])

# Generator 생성 : 다음 데이터를 제공할 최소한의 정보를 가지고 있으므로 메모리 사용량이 적다.
import array # Flat형이면서 가변형이다.

# Generator : 한 번에 한 개의 항목을 생성 (메모리 유지 X)
tuple_g = (ord(s) for s in chars) # 위에서 리스트형으로 작성되었던 것에서 소괄호로 바꾸면 generator 형태이다.
array_g = array.array('I', (ord(s) for s in chars))

print(type(tuple_g)) # 디음값을 반환할 준비가 되어있는 상태이다.
print(next(tuple_g)) # next() 명령어를 사용하면 generator 형태의 데이터 값을 가져올 수 있다. (여러번을 사용하면 StopIteration 오류로 더 이상의 값이 없다는 오류가 출력된다.)
print(type(array_g))
print(array_g.tolist()) # .tolist() : array 형식을 list 형태로 출력하는 메소드

# Generator 예제
print(('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1,21)))

for s in ('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1,21)):
    print(s)

# 리스트 주의 : 깊은 복사, 얕은 복사 -> 매우 중요함!!
marks1 = [['~'] * 3 for _ in range(4)] # '~' 3개 가지고 있는 리스트가 4개가 있는 리스트 : _를 사용하여 굳이 변수를 안사용하여도 된다.
marks2 = [['~'] * 3] * 4

print(marks1)
print(marks2)

# 수정
marks1[0][1] = 'X' # 이는 넓은 리스트 안에 첫번째 원소인 리스트의 1번 원소만 'X'로 수정되었지만
marks2[0][1] = 'X' # 이는 넓은 리스트의 모든 원소 리스트의 1번 원소가 전부 'X'로 수정되었다.

print(marks1) # marks1은 넓은 리스트 안에 있는 각 원소 리스트의 id값이 하나하나 다르므로 0번 원소리스트의 1번쨰 원소만 바뀐 것이다.
print(marks2) # marks2는 원소 리스트 자체를 복사한 것이므로 모든 id값이 일치하므로 모든 원소가 바뀌는 것이다.

# 증명
print([id(i) for i in marks1]) # marks1의 원소의 id값이 모두 다른 것을 알 수 있다.
print([id(i) for i in marks2]) # marks2의 원소의 id값이 모두 같은 것을 알 수 있다.
