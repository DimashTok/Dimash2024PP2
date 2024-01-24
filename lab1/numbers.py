"""
В Python есть три числовых типа:

int
float
complex
"""
x = 1    # int
y = 2.8  # float
z = 1j   # complex



"""
Int или целое число — это целое число, 
положительное или отрицательное, без десятичных знаков, неограниченной длины.
"""
x = 1
y = 35656222554887711
z = -3255522



"""
Число с плавающей запятой или «число с плавающей запятой» — это число,
 положительное или отрицательное,
 содержащее один или несколько десятичных знаков.
"""
x = 1.10
y = 1.0
z = -35.59

#Числом с плавающей запятой также могут быть научные числа с буквой «е», обозначающей степень 10.
x = 35e3
y = 12E4
z = -87.7e100



#Комплексные числа записываются через мнимую часть через букву «j»:
x = 3+5j
y = 5j
z = -5j


#можно преобразовать один тип в другой с помощью методов int(), float()и complex():
x = 1    # int
y = 2.8  # float
z = 1j   # complex
#convert from int to float:
a = float(x)
#convert from float to int:
b = int(y)
#convert from int to complex:
c = complex(x)
print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))


"""
В Python нет random()функции для создания случайных чисел,
 но в Python есть встроенный модуль random,
 который можно использовать для создания случайных чисел:
"""
import random
print(random.randrange(1, 10))