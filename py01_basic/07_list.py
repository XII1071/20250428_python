'''
 list  순서 있고 중복 허용, muttable
 다양한 자료형을 순차적으로 저장하는 집합적 자료형
'''

list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, ]
print(id(list_a))
list_a = list(range(1, 10))
print(id(list_a))
print(type(list_a))

list_b = ["Love", 'is', "Great", "and", "Holy"]
list_c = list_a + list_b
print(list_c, type(list_c))

# list의 원소에 접근하기
print(list_a)
print(list_a[0])
print(list_b)
print(list_b[2])
for idx in range(len(list_a)):  # 인덱스로 접근
  print(list_a[idx], end=' ')
  if idx == len(list_a) - 1: print()
for item in list_a:  # 원소에 접근
  print(item, end=' ')
print("hello")
print(list_a[0:3])
print(list_a[:3])
print(list_a[:])  # 전체 출력
print(list_a[5:20])  # 인덱스가 넘어가도 에러발생 없음
print(list_a[5:8])  # 끝자리 제외
print(list_a[-1])
print(list_a[-2])
print(list_a[-4:-2])

# range(start, stop, step)
for i in range(len(list_a) - 1, -1, -1):
  print(list_a[i], end=' ')
  if (i == 0): print()

for item in reversed(list_a):
  print(item, end=' ')
print()

print(f"{'list의 연산':=^20}")
a = [1, 2, 3]
b = list(range(3, 7))  # list()와 range()로 list생성
print(a, ',', b)

# print(a - b) # 차 X
print('a+b',a + b)
print('b+a',b + a)
print(a * 3)

print(len(a))
b[0] = 0  # 수정
print(b)

del b[0]  # 삭제 indexing
print(b)

del b[0:]  # 삭제 slicing
print(b)

print(f"{'list의 메서드':=^20}")
arr = [1,2,3,4,5,6,7,8,9,10]
print(">>>",arr);print(arr[9]);print(arr[:]);print(arr[1:3])
print(arr)

l = list();
l.append(1);  # 끝에 추가
print("l",l)
l.insert(9, 2);  # 원하는 곳에 추가
print("l",l)
l.extend([3, 4, 5])  # list를 추가
print("l",l)
l = l + [6, 7]
print("l",l)
del l[len(l) - 1]; # 마지막 인덱스를 지움
print("l",l)
del l[l.index(6)];
print("l",l)# index(원소) 해당 원소가 있는 위치를 인덱스로 반환
l.remove(5)  # 4라는 원소를 찾아서 지움
print("l",l)
l.pop()
print("l pop",l)

l = [5, 6, 7];
l.clear()  # 모두 삭제
for i in range(0, 10, 1):
  l.append(i)
print(l, id(l));
print(l[0]);
print(l[0:3])
l.append("hello")
l.append(True)
l.append(12.34)
lcopy = l.copy()  # 새로운 주소의 리스트를 생성, 주소가 다름
print(lcopy, id(lcopy))


print(f'{"2차원배열":=^30}')
lists = [
  ['홍길동', '90', '100', '90'],
  ['고길동', '91', '90', '90'],
  ['강길동', '89', '95', '90'],
  ['김길동', '70', '92', '90'],
]
print(lists)
print(lists[0])
print(lists[1][3])

print(f'{" 이중 for문 ":=^20}')
for row in lists:
  for col in row:
    print(f'{col:>3s}', end=' ')
  print()
print()

# 2차원 list 크기 초기화
lists2 = [[0 for col in range(5)] for row in range(5)]

# 배열의 길이 값 = 배열의 행의 길이 값
# 배열의 0번째 행의 길이 값 = 배열의 열의 길이 값
for i in range(len(lists2)):
  for j in range(len(lists2[i])):
    if i < len(lists2) - 1 and j < len(lists2[i]) - 1:
      lists2[i][j] = lists[i][j]
      if j != 0:
        lists2[i][len(lists[i])] += int(lists[i][j])
        lists2[len(lists)][j] += int(lists[i][j])
        lists2[len(lists)][len(lists[i])] += int(lists[i][j])
    if j == 0:
      if i == len(lists2) - 1: lists2[i][j] = "총합계"
      print("{0:3}".format(lists2[i][j]), end="")
    else:
      # print("{0:>4}".format(lists2[i][j]), end=" ")
      # print("%4s" % lists2[i][j], end=" ")
      print(f"{lists2[i][j]:>4}", end=" ")
  print()
print()