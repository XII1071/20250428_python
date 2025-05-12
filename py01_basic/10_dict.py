# dict (키를 이용하여 값을 저장하는 자료형)
# 정수형 인덱스가 아닌 키로 값을 저장하기 때문에 저장된 순서는 무의미
# key(immutable)는 중복 불가, value(mutable)는 중복 가능

d = dict()
print(d, type(d))
d = {}
print(d, type(d))
d = {"a": 1, "b": 2, 'c': 3}
print(d)
d['a'] = 10
print(d)
d['d'] = 4
# print(d['k']) #없는 key는 에러
print(d.get('k', 100)) #없는 경우 default 적용
print(d.keys())
print(d.values())
tmp = list(d.values())
tmp = [i for i in d.values()]
print(tmp, type(tmp))
print(d.items())

for k in d:
  print(k, d[k], sep=",", end="/")
print()
for k in d.keys():
  print(k, d.get(k), sep=",", end="/")
print()
for v in d.values():
  print(v, sep=",", end="/")
print()
# setdefault는 추가만, update는 수정, 추가 가능
d.setdefault('e') # value 없이 넣을 경우 값은 None
print(d)
d.setdefault('f', 5) # value 없이 넣을 경우 값은 None
print(d)
d.update(a='One', g = 6)
print(d)
print(d.pop('a'))
print(d.pop('z', 100))
print(d)
del d['g']
print(d)
print(d.popitem()) #python 3.6이상에서는 맨끝, 이하에서는 임의
# print(d)
d.clear()
print(d)


print()
print()
print()
print()
print()
print()
print()
print()
print()