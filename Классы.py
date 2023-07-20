'''
Создание из класса объекта. Обращение к элементу.
'''

class MyClass:
    x = 5
object = MyClass()
print('Пример 0.0:\n', object.x)

'''
__init__   Инициализация свойств класса для представления свойства значений
'''
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
man = Person('Egor', 12)
print('Пример 1.0: \n', man.name, man.age)


'''
__str__   функция используется если возвращается только строка
'''
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f'{man.name} {man.age}'
man = Person('Egor', 12)
print('Пример 1.1: \n', man)


'''
Методы объектов как функции
'''
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myFunction(self):
        print('Пример 2.0: \n', f"Hello, I'm {self.name}")
man = Person('Egor', 12)
man.myFunction()


'''
Можете назвать переменную инициализации как хотите
'''
class Person():
    def __init__(randomVar, name, age):
        randomVar.name = name
        randomVar.age = age
    def myFunction(absltRandom):
        print('Пример 3.0: \n', f"Hello, I'm {absltRandom.name}")
man = Person('Egor', 12)
man.myFunction()


'''
Добавление, изменение и удаление свойств в объекте
'''
man.birthday = '2000.10.02'
print('Пример 4.0: \n', man.birthday)

man.birthday = '2011.03.14'
print('Пример 4.1: \n', man.birthday)

# del man.birthday

# del man


'''
Пустой класс, чтобы избежать ошибок
'''
class Person():
    pass