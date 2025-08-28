#Числа и арифмитические операции

# 1 задание
a = 6
b = 5
x = 4.6
y = 8.453

print(type(a))
print(type(b))
print(type(x))
print(type(y))

# 2 задание

num1 = 5
num2 = 2

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 // num2)
print(num1 ** num2)

# 3 задание

a = 10
b = 3

oper1 = a / b
oper2 = a // b
oper3 = a % b
print(oper1, oper2, oper3)

a = -10
b = 3

oper1 = a / b
oper2 = a // b
oper3 = a % b
print(oper1, oper2, oper3)

a = 10
b = -3

oper1 = a / b
oper2 = a // b
oper3 = a % b
print(oper1, oper2, oper3)

# 4 задание
a = 5 + 3 * 2
b = (5 + 3) * 2
c = 10 / 2 ** 2

print(a, b, c)

# 5 задание
count = 10
count += 5
count -= 3
count *= 2
count /= 4
print(count)

#___________________________________________________________________
# Строки в Python
# 1 задание
s1 = "Python"
s2 = "Программированние"
print(s1, s2)
s3 = """ 
 Python
 Программированние
 """
print(s3)

empty = ""
print(len(empty))

# 2 задание
first_name = "Иван"
last_name = "Петров"

full_name = first_name + " " + last_name
print(full_name)

# 3 задание
s = "Возраст"
age = 25

s1 = s + str(age)
print(s1)

# 4 задание
str1 = "ха "
print(str1 * 5)
print(str1 * 2.5) #ошибка так как число не integer

# 5 задание
text = "Привет Мир!"
print(len(text))
text1 = ""
print(len(text1))

# 6 задание
sentence = "Я изучаю Python"
print( "Python" in sentence)
print( "Java" in sentence)

# 7 задание
a = "apple"
b = "banana"

print(a == b)
print( a != b)
print( a < b)
print( a > b)
print( a >= b)
print( a <= b)

# 8 задание
print(ord("А"))
print(ord("а"))
print(ord("я"))
