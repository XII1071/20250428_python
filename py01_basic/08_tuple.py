# tuple: ()를 사용, 순서 있고 중복 허용. immutable(생성, 삭제, 수정이 안됨)
# 상수 적인 특성을 가지고 있기 때문에 list 보다 연산이 빠름.

t = (1, 2, 3) # 튜플 리터럴
print(1, t, type(t))
t = tuple() # tuple(): 파이썬에서 튜플을 생성하는 내장 함수(빈 튜플)
print(2, t, type(t))
t = tuple([1, 2, 3]) # tuple(): 튜플형으로 변환하는 함수
print(3, t, type(t))
t = tuple("abc")
print(4, t, type(t))

t1 = (); print("t1", type(t1))
t2 = (2); print("t2", type(t2))
t2 = (1,); print("t2", type(t2))  # tuple에서 1개 자료만 있는 경우 뒤에 ,를 찍어라
t3 = (1, 2); print("t3", type(t3))
t4 = 1, 2, 3; print("t4", type(t4))
t5 = ('a', 'b', ('ab', 'cd')); print("t5", type(t5))

for item in t5:
  print(item, end=', ')
print()
for i in range(0, len(t5)):
  print(i, t5[i], sep=")", end=' ')
print()

# t4[0] = 0; #immutable type
# del t4[0]; #immutable type
print(type(range(10)))
t1 = tuple(range(10))
t1 = tuple(range(2, 10))
t1 = ((1 for col in range(4)) for row in range(3))
print("t1: ", type(t1))
t1 = tuple(tuple(1 for col in range(4)) for row in range(3))
print(f'{" 이중 for문 ":=^20}')
for r in t1:
  idx = 0
  for item in r:
    if idx != 0:
      print(",", end=' ')
    idx += 1;
    print(f"{item:>2d}", end="")
  print()

for i in range(len(t1)):
  for j in range(len(t1[i])):
    print(f"{item:>2d}", end="")
  print()

print(f'{" 인덱싱하기 ":=^20}')
t1 = (1, 2, 'a', 'b')
print(t1[0])
print(t1[3])
print(t1)

print(f'{" 슬라이싱하기 ":=^20}')
print(t1[1:])

print(f'{" 튜플 더하기 곱하기 ":=^20}')
t1 = (1, 2, 'a', 'b',)
t2 = 3, 4,
t3 = t1 + t2
print(t3) # tuple을 합친게 아니고 재정의 함.
t4 = t2 * 2
print(t4)
print(len(t1))