import math

#level one
from ast import Import
import math


def multiply(num):
    num = num*3
    return num
def count(str):
    y= len(str)
    return y
    
    
x = multiply(3)
print(x)
y = count("Ahmed")
print(y)

#level two
sqr = lambda z: math.sqrt(z)
print(sqr(4))

check = lambda l: l%2==0
print(check(3))

#level three
nums = [1, 7, 12, 15, 22, 28]
great = list(filter(lambda m:m>10,nums))
print(great)

names = ["Ahmed", "Ali", "Amira", "Sara", "Ayman"]
start = list(filter(lambda m:m.startswith("A"),names))
print(start)