'''
Итератор - это объект, по которому можно выполнять итерации,
что означает, что вы можете перемещаться по всем значениям.

iter() - создание итераторва
next() - след. элемент

for var in object:
    print(var)
'''
mytuple = ("яблоко", "банан", "вишня")
myit = iter(mytuple)

print(type(myit))

print(next(myit))
print(next(myit))
print(next(myit))

'''
Строки также являются итерируемыми объектами
'''
myStr = iter('banana')

print(f'{next(myStr)}\n{next(myStr)}\n{next(myStr)}\n{next(myStr)}\n{next(myStr)}')


'''
Создание итетора в объекте
'''
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
        x = self.a
        self.a += 1
        return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)