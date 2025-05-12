# Python: script언어, 소스 코드를 한줄 씩 읽어 바로 실행하는 Interpreter방식
print("Python print()에 대하여 알아 봅시다.")

print('hello world')
print(True, 3.14, 'Python')
print("\\ , \t, \', \", \n  ")
print() # 빈줄 :: 한줄 내려쓰기
print("hello\tworld\n")
print("그 때였다 갑자기 문이 열리면 '배달왔어요' ")
print("그 때였다 갑자기 문이 열리면 \"배달왔어요\" ")
print('그 때였다 갑자기 문이 열리면 \"배달왔어요\" ')
print('그 때였다 갑자기 문이 열리면 \'배달왔어요\' ')
print("""저 산자락에 긴 노을 지면
걸음 걸이도 살며시 달님이 오시네
""")
print('''해 뜨는 동해에서
해지는 서해까지
뜨거운 남도에서 
광활한 만주 벌판 
''')

# {}개수 <= 매개변수. {}의 갯수와 매개변수의 갯수는 일치하거나 커야 한다.
# print("{0:=v20}".format('format()'))
print("{} {}".format(10, 20, 30))
print("{}".format("Python"))
print("{0:=^20}".format('format()'))
print("{0:=<20}".format('format()'))
print("{0:=>20}".format('format()'))
print("{0:=^20}".format('Python'))
print("{0:^20}".format('특수문자'))

print("{}".format(-10))
print("{:-d}".format(10))
print("{:+d}".format(10))
print('{:+8d}'.format(123))  # +123
print('{:=+8d}'.format(123))  # + 123
print('{:+08d}'.format(123))  # +0123
print('{:=+08d}'.format(123))  # +0123
print('{:=-8d}'.format(-123))  # +0123
print('{:=-8d}'.format(-123))  # +0123
print('{:8f}'.format(3.141592))  # 소수포함 8자리
print('{:8.2f}'.format(3.141592))  # 소수포함 8자리
print('{:8.3f}'.format(3.141592))  # 반올림 발생
print("{{}}는 클래스".format())

print(f'{"f 포맷":=^20}')
print("{0:=^20}".format("f 포맷"))
print(f'{"f 포맷":=^20}')
print(f'f 포맷')
print(f'{10}')
print(f'{"Hello Python"}')
print(f'3.141592:0.4f는 출력 되면 {3.141592:0.4f}')
print(f'{len("Hello Python")}')

city = 'Busan'
print(f'내가 사는 곳 {city}')
print("내가 사는 곳 {}".format(city))

d = {'city': 'Busan', 'year': 2025}
print("{}년 내가 사는 곳 {}".format(d['year'], d['city']))
print(f'{d['year']}년 내가 사는 곳 {d["city"]}')
print("%d년 내가 사는 곳 %s" % (d['year'], d['city']))

'''
print의 속성 : self, *args, sep='', end='\n', file=None
'''
print('hello')  # self
print(1, 2, 3, 4, 5)  # args
print(1, 2, 3, 4, 5, sep='🚀')  # args
for i in range(10):
  print(i, end='\n')
print()

with open('test.txt', 'w') as f:
  print('큰 바다 있고 푸른 하늘 가진 \
  \n이 땅 위에 사는 나는 행복한 사람 아니냐', file=f) # file
f = open('test.txt', 'r')
lines = f.readlines()
for line in lines: print(line, end='')






