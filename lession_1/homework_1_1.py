#1 задание
name = "Алексей"
age = 35
height = 1.76
print("Моё имя:", name)
print("Мой возраст:", age, "лет" )
print("Моё рост:", height, "метров")

#2 задание
x = 10
print(x)
x = 25.5
print(x)
x= "Python"
print(x)

#3 задание
a = 7
b = a
print(a)
print(b)
a = 10
print(b)
# Чтение кода происходит сверху вниз поэтому переменная b получает первое значение переменной a. Про переменную a
# которая находится ниже она даже не знает

#4 задание
x = y = z = 100
print(x, y, z)
print(id(x), id(y), id(z)) #одинаковые
x = 23
y = 54
z = 32
print(x, y, z)
print(id(x), id(y), id(z)) #разные

#5 задание
a = 5
b = 10
a, b = b, a
print(a, b)

#6 задание
#невозможно создать заредервированные слова в качестве переменных
import keyword
print(keyword.kwlist)

#7 задание
var1 = 42
var2 = 3.14
var3 = "Hello"
print(type(var1))
print(type(var2))
print(type(var3))
var1 = "Домашнее задание"
print(type(var1))

#8 задание
name_kids1 = "Виктория"
name_kids2 = "Мария"
age_kids1 = 11
age_kids2 = 4
height_kids1 = 1.53
height_kids2 = 1.01

print(name_kids1, type(name_kids1))
print(name_kids2, type(name_kids2))
print(age_kids1, type(age_kids1))
print(age_kids2, type(age_kids2))
print(height_kids1, type(height_kids1))
print(height_kids2, type(height_kids2))

Число = 10
#Работает