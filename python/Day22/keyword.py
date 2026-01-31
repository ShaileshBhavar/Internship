# if
# while
# for
# function

name="a2z";



""" variable-(storage) """
# var name=value
# name=value datatype-auto
# rules
# my name=
# 12abc=
# ab-cd=

a=100;
b=100;
c=a+b;
print(c);


""" Datatypes """
a=10
b=3.14
name="shailesh"
number=[1,2,3]
point=(10,20)
unique={1,2,3}
student={"name":"shailesh", "age":21}
print(a, b, name, point, unique, student)


""" I/P and O/P """
name=input("enter your name: ")
age=input("enter your age: ")
print("Name:", name)
print("Age:", age)

name = "shailesh"
age = 21

print(f"My name is {name} and my age is {age}")

""" Operators """
a = 10
b = 3

print(a + b)   # Addition
print(a - b)   # Subtraction
print(a * b)   # Multiplication
print(a / b)   # Division
print(a % b)   # Modulus

""" Relational & Logical Operators """
print(a > b)
print(a == b)
print(a > 5 and b < 5)

""" Control Statement """
num = 10

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")


marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Grade C")


""" Loop Control Statement """
for i in range(1, 6):
    print(i)

i = 1
while i <= 5:
    print(i)
    i += 1   

for i in range(1, 6):
    if i == 3:
        continue
    print(i)  

for i in range(1, 6):
    if i == 4:
        break
    print(i)   

for i in range(5):
    pass