'''
Примером функции Python, которая может использоваться на разных объектах,
является len() функция.
'''
# String
x = 'random x'
print(len(x))
# Tuple
x = ('apple', 'banana', 'orange')
print(len(x))
# Directory
x = {
    'a': 1,
    'b': 2,
}
print(len(x))


'''
Полиморфизм классов
'''
class Zaeb:
    def __init__(self, name):
        self.name = name
    def move(self):
        print(f'Ты, {self.name}, заебал!')

class Good:
    def __init__(self, name):
        self.name = name
    def move(self):
        print(f'{self.name}, как дела?')

obj1 = Zaeb('Gena')
obj2 = Good('Egor')
# Посмотрите на цикл for в конце.
# Благодаря полиморфизму мы можем выполнить один и тот же метод для всех трех классов.
for i in (obj1, obj2):
    i.move()


'''
Полиморфизм классов наследования
'''
class words:
    def __init__(self, name):
        self.name = name
    
    def move(self):
        print('Sho') 
    
class Zaeb(words):
    def move(self):
        print(f'Ты, {self.name}, заебал!')

class Good(words):
    def move(self):
        print(f'{self.name}, как дела?')

obj1 = Zaeb('Gena')
obj2 = Good('Egor')
obj3 = words('gena')

for i in (obj1, obj2, obj3):
    i.move()