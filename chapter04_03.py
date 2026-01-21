# Chapter04-3
# 파이썬 반복문
# While 실습

# while <expr>:
#   <statement(S)>
# 즉, 조건에 만족할 때까지 반복

# 예제1
n = 5

while n > 0:
    n = n - 1
    print(n)

# 예제2
a = ['foo', 'bar', 'baz']

while a:
    print(a.pop())

print()

# break, continue 사용

# 예제3
# break
n = 5

while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print('Loop Ended.')

# 예제4
# continue
m = 5

while m > 0:
    m -= 1
    if m == 2:
        continue
    print(m)
print('Loop Ended.')

print()

# if 중첩
# 예제5
i = 1

while i <= 10:
    print('i: ', i)
    if i == 6:
        break
    i += 1

print()

# while - else 구문
# 예제6
n = 10

while n > 0:
    n -= 1
    print(n)
else:
    print('else out.')

# 예제 7
a = ['foo', 'bar', 'baz', 'qux']
s = 'kim'

i = 0

while i < len(a):
    if a[i] == s:
        break
    i += 1
else:
    print(s, 'not found in list.')

print()

# 무한반복
# while Trie:
#       print('Foo')

# 예제8
a = ['foo', 'bar', 'baz']

while True:
    if not a:
        break
    print(a.pop())

print()