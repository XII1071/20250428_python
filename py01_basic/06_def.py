# def : define
# 중복된 코드를 줄일 수 있고, 코드의 가독성을 높이고, 유지보수성을 향상
# Processing 들의 묶음
'''
def 함수이름(매개변수1, 매개변수2, ...):
    함수본문
    return 반환값
'''

# 1) 함수 정의(매개변수 없고, 리턴타입 없음)
def lines():
  print("==" * 12)
lines()

# 2) 함수 정의(매개변수 있고, 리턴타입 없음)
def lines(str):
  print(f'{" " + str + " ":=^30}')
# lines() # 에러: 파이썬에는 overloading이 없기 때문에 최종 함수로 적용
lines("Title")

# 3) 함수 정의(매개변수가 없고, 리턴타입 있음)
def lines():
  return f"{'':=^30}"
print(lines())

# 4) 함수 정의(매개변수가 있고, 리턴타입 있음)
def lines(str):
  return f"{" " + str + " ":=^30}"
print(lines("python"))

# default arguments, positional arguments
def calculator(a, b, c=0):
  return a + b + c
print(calculator(1, 2))
# print(calculator(1)) positional argument error

total = 0
# 가변 위치 매개변수 (*args) 복수의 데이터를 받는 형태
def add(*arg):
  print(type(arg))  # arg는 tuple 타입
  global total  # 지역변수이지만 전역변수를 끌어올 때
  for item in arg:
    total += item
  return total

print(add(1, 2, 3, 4, 5, 6))
print(add(1, 2, 3, ))
print(add(1))

# 가변 키워드 매개변수(**kwargs) key와 value형태
def print_info(**kwargs):
  for key, value in kwargs.items():
    print(f"{key}: {value}")

print_info(name="Alice", age=25)

def f1(): print(var)
def f2():
  print()
  var = 10;
  print(var)

def f3(inputVar):
  global var # global 위치에 상관없이 변수 호출가능
  var = inputVar
  print("local var",var)

var = 100
f1()
f2()
f3(10000)
print(var)


def print_all_elements(list_of_things):
  ## 중첩함수 선언
  def print_each_element(things):  # 리스트 요소를 하나씩 꺼내주는 함수
    for thing in things:
      print(thing, end= ' ')
    print()

  if len(list_of_things) > 0:
    print_each_element(list_of_things)
  else:
    print("There is nothing!")

print_all_elements([1, 2, 3, 4, 5, 6])

# 중첩함수가 부모 함수의 변수나 정보를 가두어 사용하는 것을 Closure
def outer(x):
  def inner(y):
    return x + y
  return inner

add_five = outer(5)
print("중첩", add_five(3))
print("중첩", add_five(3))
print("중첩", add_five(3))
print("중첩", add_five(3))
print("중첩", add_five(3))


# 람다 함수 (익명 함수)
square = lambda x: x ** 2
print(square(4))

# Decorator: 기존 함수 수정하지 않고 기능을 추가하는 함수. 클로저와 고차 함수가 기반
# @my_decorator는 say_hello = my_decorator(say_hello)와 같음
def my_decorator(func):
  def wrapper():
    print("Before function")
    func()
    print("After function")
  return wrapper

@my_decorator
def say_hello():
  print("Hello ")
  print("World!")

say_hello()





