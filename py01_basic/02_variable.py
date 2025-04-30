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

del a # 변수를 더 이상 사용하지 않을 때
# print(a, type(a))

a = 12.34567890123456789 # 소수 15째자리(절삭)
print(a, type(a))
print(int(a), type(int(a)))
print('기존 값: a=%f' % a) # 소수 6째자리(반올림)
print('기존 값: a={}'.format(a) )
print(f'기존 값: a={a}') # f-string을 이용한 출력
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
print(123e2, type(123e2))
print(123e-2, type(123e-2))

print(f"{"complex":=^20}")
a = 10 + complex(3)
print(a, type(a))
print(a.real, a.imag)

print(f"{"None":=^20}")
print(type(None), None)
print('' is None)
a = None
a: int | None #Python 3.10 이상
a = True
print(a, type(a))

print("%s" % "논리형")
print("{0:=^20}".format("논리형"))
print(f"{"논리형":=^20}")
print(a=False)
print(a == False)
print(bool(-1))
print(bool(0))
print(bool(1))











