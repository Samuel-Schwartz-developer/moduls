'''
Модуль — это библиотека или импорт данных из другого файла
'''
import lambda_function
lambda_function.x(2)


'''
Так и с переменными
'''
import Классы
Классы.man.myFunction()


'''
Можно поменять имя модуля через слово as
'''
import lambda_function as lmbd
lmbd.x(3)


'''
Встроенные модули
'''
import platform

x = platform.system()
print(x)
