# Чтение файла. Стоит по стандарту('r')
# Конструкция open('имя', 'r')
# file = open('readme.txt')
# info = file.read() можно указать кол-во символов необходимых для чтения
# print(info)
# или
# print(*file)
# file.close()

# Запись в файл. Мод 'w'
# file = open('readme.txt', 'w')
# file.write('Text from my job')
# file.close()

# with гарантирует закрытие файла
# with open('readme.txt', 'w') as file:
#     file.write('Nice day today')

# При попытке записать в image файл — получите исключение
