# Chapter02-1
# 피이썬 완전 기초
# Print 사용법

# 기본 출력
print('Python Start!')
print("Python Start!")
print('''Python Start!''')
print("""Python Start!""")

print()

#seperator 옵션
print('P', 'Y', 'T', 'H', 'O', 'N', sep='')
print('P', 'Y', 'T', 'H', 'O', 'N', sep='|')
print('P', 'Y', 'T', 'H', 'O', 'N', sep='    ')
print('010', '7777', '1234', sep='-')
print('python', 'google.com', sep='@')

print()

# end 옵션
print('Welcome to', end=' ')
print('IT News', end=' ')
print('Web Site')

print()

# file 옵션
import sys

print('Learn Python', file=sys.stdout)

print()

# format 사용(d, s, f)
# d -> 정수, s -> 문자열, f -> 실수
# d : 3, s : 'python', f : 3.14159
print('%s %s' % ('one', 'two'))
print('{} {}'.format('one', 'two'))
print('{1} {0}'.format('one', 'two')) 

print()

# %s
print('%10s' % ('nice'))
print('{:>10}'.format('nice'))

print('%-10s' % ('nice'))
print('{:10}'.format('nice'))

print('{:_>10}'.format('nice'))
print('{:^10}'.format('nice'))

print('%.5s' % ('nice'))
print('%.5s' % ('pythonstudy'))

print('%5s' % ('nice'))
print('%5s' % ('pythonstudy'))

print('{:10.5}'.format('pythonstudy'))

print()

# %d
print('%d %d' % (1, 2))
print('{} {}'.format(1, 2))

print('%4d' % (42))
print('{:4d}'.format(42))

print()

# %f
print('%f' % (3.14343434))
print('%1.18f' % (3.14343434))
print('{:f}'.format(3.14343434))

print('%06.2f' % (3.141592653589793))
print('{:06.2f}'.format(3.141592653589793))