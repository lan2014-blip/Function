def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

choice=input("enter which opreration you want to perform add, subtract, multiply, divide")
num1=int(input("enter fist number"))
num2=int(input("enter second number"))

if choice=="add":
    print("the addtion of", num1,"and", num2,"is", add(num1,num2))

if choice=="subtract":
    print("the subtractino of", num1,"and", num2,"is", subtract(num1,num2))

if choice=="multiply":
    print("the multiplication of", num1,"and", num2,"is", multiply(num1,num2))

if choice=="divide":
    print("the divisio of", num1,"and", num2,"is", divide(num1 and num2))