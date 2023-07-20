# Обработка и вывод ошибки исключения
# print("start")
# try:
#    val = int(input("input number: "))
#    tmp = 10 / val
#    print(tmp)
# except Exception as e:             
#    print("Error! " + str(e))
# print("stop")

# Обработка нескольких исключений
# 1 вариант
# print("start")
# try:
#    val = int(input("input number: "))
#    tmp = 10 / val
#    print(tmp)
# except(ValueError, ZeroDivisionError):
#    print("Error!")
# print("stop")
# 2 вариант
# print("start")
# try:
#    val = int(input("input number: "))
#    tmp = 10 / val
#    print(tmp)
# except ValueError:
#    print("ValueError!")
# except ZeroDivisionError:
#    print("ZeroDivisionError!")
# except:
#    print("Error!")
# print("stop")

# передача подробную информацию о произошедшем исключении
# print("start")
# try:
#    val = int(input("input number: "))
#    tmp = 10 / val
#    print(tmp)
# except ValueError as ve:
#    print("ValueError! {0}".format(ve))
# except ZeroDivisionError as zde:
#    print("ZeroDivisionError! {0}".format(zde))
# except Exception as ex:
#    print("Error! {0}".format(ex))
# print("stop")

# код при finally всё равно будет выполнен, можно и else
# try:
#    val = int(input("input number: "))
#    tmp = 10 / val
#    print(tmp)
# except:
#    print("Exception")
# finally:
#   print("Finally code")

# принудительная генерация исключений
# try:
#    raise Exception("Some exception")
# except Exception as e:
#    print("Exception exception " + str(e))

