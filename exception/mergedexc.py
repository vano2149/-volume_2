"""
mergedexc.py file!
"""

sep = '-' * 45 + '\n'

print(sep + 'EXEPTION RAISED AND CAUGHT')
try:
    x = 'spam'[99]
except IndexError:
    print('except run')
finally:
    print('finally run')
print('after run')

#Здесь Исключение не генерируется
print(sep + 'NO EXCEPTION RAISED')
try:
    x = 'spam'[3]
except IndexError:
    print('except run')
finally:
    print('finally run')
print('after run')

#Здесь не генерируетя Исключение, c с конструкцией else!
print(sep + 'NO EXCEPTION RAISED, WITH ELSE')
try:
    x = 'spam'[3]
except IndexError:
    print('except run')
else:
    print('else run')
finally:
    print('finally run')
print('after run')

# Исключение генериуется Но не перехватывается!
print(sep + 'EXEPTION RAISED BUT NOT CAUGTH')
try:
    x = 1 / 0
except IndexError:
    print('except run')
finally:
    print('finally run')
print('after run')
