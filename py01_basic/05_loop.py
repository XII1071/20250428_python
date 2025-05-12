print("{0:=^20}".format("반복문"))
print(f'{"반복문":=^20}')
'''
for 변수 in 리스트(또는 튜플, 문자열):
  수행 문장1
  수행 문장2
  ...
'''

ls = ['one', 'two', 'three']
for i in ls:
  print(i)  # 원소를 직접 다룸

for i in range(len(ls)):
  print(ls[i], ', index:', ls.index(ls[i]))  # 리스트의 인덱스를 이용한 접근

a = [(97, 'a'), [98, 'b'], (99, 'c')]
for (k, v) in a:
  print("{} : {}".format(v, k), end="\n")

for i in range(97, 97 + 26):
  if (i != 97): print('', end=',');
  print(chr(i), end='');
  if(i == 97+25): print();

marks = [90, 25, 67, 45, 80]
print('marks에서 60점 이상인 점수만 출력하시오')
for mark in marks:
  # if mark > 60: print(mark)
  if mark < 60: continue
  print(mark)

a = "12ㄱ345"
if a.isnumeric():
  print(type(a))
else:
  print("Not a Number")

for i in a:
  # try:int(a)
  # except:result = "Not a Number";break;
  if not i.isnumeric(): result = "Not a Number";break;
  # if (ord(i) < ord('0') or ord(i) > ord('9')):
  #   result = "Not a Number";break;
print(result)

for i in a:
  if i.isnumeric(): print(i)
  else: continue

print(f'{"구구단":=^20}')
for i in range(2,10):
  for j in range(1,10):
    print(f'{i}*{j}={i*j}')
  print()

# range(start, stop, step)
for i in range(2, 10, 3):
  for j in range(1, 10):
    for k in range(0, 3):
      if not ((i + k) == 10):
        print(f'{i + k} * {j} = {(i + k) * j:2d}', end='\t')
    print()
  print()

for i in range(1, 5):
  print(i, end=', ')
else:
  print("모든 원소 출력")

for i in [1,2,3,4]:
  if i % 3: print(i)
  else: break # for의 else문은 실행되지 않음
else: # 문제가 생기면 for의 else문은 실행 안됨.
  print("모든 원소 출력")

for i in [1,2,3,4]:
  if i % 3: print(i)
  else: break
print("모든 원소 출력")

a = list(range(1, 10))
print("a:",a)

i = 0
while i < len(a):
  print("짝수" if a[i] % 2 == 0 else "홀수", end=' ');
  i += 1

print()

i=0
while(i<5):
  i+=1
  if i % 3 == 0: break
  print(i)
else:
  print("💥1~4까지 모든 숫자가 출력")

# Python에는 do while문이 없다.
secret_word = "python"
counter = 0

while True:  # 무조건 1번은 실행
    word = input("암호를 입력하세요: ").lower()
    counter = counter + 1
    if word == secret_word:
      print("Well done!")
      break
    if word != secret_word and counter > 7:
      break




