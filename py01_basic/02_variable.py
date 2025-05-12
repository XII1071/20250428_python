# 변수의 명명규칙
# 1) 예약어 안됨
# 2) -, 영문자(대소문자 구별), 숫자(시작 안됨)
# 3) 특수문자, 공백 안됨
# 4) 변수나 함수는 Snake case, 클래스는 Pascal
# 5) Python에서는 null 대신 None 사용

'''
=== 파이썬 변수의 자료형 ===
불 자료형: True, False
숫자 자료형: int, float, complex
군집 자료형: str, list, tuple, dict, set
동적 자료형: 입력시 타입이 결정(동적 할당)
동적 할당 때문에 변수에 타입을 강제적 고정 불가
'''

# 선언시 타입 없이 선언하며 초기화 될때 자료형 결정
a = 10
b = True
c = 3.14
print(type(a), type(b), type(c))
d = complex(3, -4)
e = 10 + 3j + 5J
print(type(d), type(e), d.real, d.imag)
s = 'hello'
print(s, type(s), )

# k = (a = 10 + 20) # 할당문이 다른 할당문을 포함할 수 없다.
k = a = 10 + 20
k = b = a
print(k, type(k), )
n1 = 1;
n2 = 2
print("n1 = {}, n2 = {}".format(n1, n2))
print(f'n1 = {n1}, n2 = {n2}')
print("n1 = %d, n2 = %d" % (n1, n2))

a = 1;
b = 2;
print('변수 교환전: a=%d, b=%d' % (a, b))
a, b = b, a
print('변수 교환후: a=%d, b=%d' % (a, b))

a = 10
print(a, type(a))
print(a, format(a, 'b'))
print(a, format(a, 'o'))
print(a, format(a, 'x'))
print(a, format(a, 'X'))
print(a, format(a, '#b'))
print(a, format(a, '#o'))
print(a, format(a, '#x'))
print(a, format(a, '#X'))
a = 0b1010
a = 0o12
a = 0xa
a = 0XA
print(a, type(a))

del a  # 변수를 더 이상 사용하지 않을 때
# print(a, type(a))

a = 12.34567890123456789  # 소수 15째자리(절삭)
print(a, type(a))
print('기존 값: a=%f' % a)  # 소수 6째자리(반올림)
print('기존 값: a={}'.format(a))
print(f'기존 값: a={a}')  # f-string을 이용한 출력
print(f'소수 첫번째 자리 표기: a={round(a, 1)}')
print(f'소수 두번째 자리 표기: a={round(a, 2)}')
print(f'소수 세번째 자리 표기: a={round(a, 3)}')
print(f'소수 네번째 자리 표기: a={round(a, 4)}')
print(f'소수 첫번째 자리 표기: a={a:.1f}')
print(f'소수 두번째 자리 표기: a={a:.2f}')
print(f'소수 세번째 자리 표기: a={a:.3f}')
print(f'소수 네번째 자리 표기: a={a:.4f}')
print('소수 네번째 자리 표기: a={:.4f}'.format(a))
print('소수 네번째 자리 표기: a=%.4f' % a)
print('소수 네번째 자리 표기: a=', format(a, ".4f"))
print("1)", 123e2, type(123e2))
print("2)", 123e-2, type(123e-2))

print(f"{"complex":=^20}")
a = 10 + complex(3)
print(a, type(a))
print(a.real, a.imag)

print(f"{"None":=^20}")
print(type(None), None)
print('' == None)
a = None
a: int | None  # Python 3.10 이상
a = True
print(a, type(a))

print("%s" % "논리형")
print("{0:=^20}".format("논리형"))
print(f"{"논리형":=^20}")
print(a == False)
print((1 > 2) or (2 < 5))  # True
print(1 > 2) or (2 > 5)  # False
print(1 > 2)
print(False) or (2 < 5)

print(f"{"문자형":=^20}")
print("hello", type("hello"))

print(f"{"형변환 함수":=^20}")
print("int 형변환함수", int(12.34), type(int(12.34)))
print("float 형변환함수", float(123), type(float(123)))
print("complex 형변환함수", complex(3, 4), type(complex(3, 4)))
print("bool 형변환함수 bool(-1)", bool(-1))
print("bool 형변환함수 bool(0)", bool(0))
print("bool 형변환함수 bool(1)", bool(1))
print("bool 형변환함수 bool(0.1)", bool(0.1))
print("bool 형변환함수 bool('')", bool(''))
print("bool 형변환함수 bool(None)", bool(None))
print("str 형변환함수 str(None)", str(None))
print("str 형변환함수 str(97)", str(97))
print("chr 형변환함수 chr(97)", chr(97))
try:
  b = int("a10")  # 문자열, 수치자료를 int type 변경
  b = float("a0.12")  # 문자열, 수치자료를 float type 변경
except:
  print("숫자가 아닌 문자열이 포함되어 있습니다.")

string = "abc123def456"
number_string = ""
for char in string:
    if char.isdigit():
        number_string += char
number = int(number_string)
print(number, type(number)) # 출력: 123456

string = "abc123def456"
parts = string.split()
numbers = list(filter(str.isdigit, parts))
# number = int("".join(numbers).strip())
print(numbers) # 출력: 123456

a="A";
print(ascii(a), end=' '); print(str(a), end=' '); print(ord(a));
a=65;
# chr()는 매개변수가 숫자여야만 함.
print(ascii(a), end=' '); print(str(a), end=' '); print(chr(a));

print("=" * 10)
print("Hello Python"[0])
print("Hello Python"[-3])
print("Hello Python"[0:12:3])  # [a:b:c] c폭

# python에는 상수가 없다.  python은 동적언어이기 때문에 상수가 불필요
from typing import Final
SIZE:Final = 5
SIZE = 10
print(SIZE)

import constant as const
const.PI = 3.14
print(const.PI)

# 에러 발생. 재할당이 안됨.
# const.PI = 3.141592
# print(const.PI)