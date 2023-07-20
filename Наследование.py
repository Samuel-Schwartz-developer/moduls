'''
Родительский — тот класс, от которого наследуется
Дочерний — тот класс, которому наследуется

Создаём пустой класс, но в качестве параметра определяем нужный нам класс. Теперь он делает то же

Когда вы добавляете __init__() функцию, дочерний класс больше не будет наследовать __init__() функцию родительского класса.
'''
class Person():
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f'{self.name}'


class Student(Person):
    pass

x = Student('Egor')
print(x)


'''
Использование функции super()
вместо 
Person.__init__(self, name, surname)
'''
class Person():
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    def Print(self):
        print(f'{self.name}')


class Student(Person):
    def __init__(self, name, surname):
        super().__init__(name, surname)


'''
Добавление свойств
'''
class Person():
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    def Print(self):
        print(f'{self.name} {self.surname}')


class Student(Person):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.graduationyear = 2019

x = Student('Egor', 'Goryachev')
print(x.graduationyear)
