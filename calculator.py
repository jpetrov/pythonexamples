# Python calculator v.1.0
import math

# Calculator functions

# Addition
def calc_add(x, y):
    return x + y

# Subtraction
def calc_subtract (x, y):
    return x - y

# Muultiplication
def calc_multiply (x, y):
    return x * y

# Division
def calc_divide (x, y):
    return x / y

# Exponentiation
def calc_exponent (x, y):
    return x ** y

# Square root
def calc_sqrt (x):
    return math.sqrt(x)


print('Welcome to the calculator v.1.0\n')
print('Operators\n')
print('+ = add, - = subtract, * = multiply, / = divide, ^ raise to power, s = square root\n')
choice = 'y'
while(choice == 'y' or choice =='Y'):
    number1 = float(input("x = "))
    number2 = float(input("y = "))
    operator = str(input("Operator:"))
    if(operator=='+'):
        result = calc_add(number1, number2)
    elif(operator=='-'):
        result = calc_subtract(number1, number2)
    elif(operator=='/'):
        result = calc_divide(number1, number2)
    elif(operator=='*'):
        result = calc_multiply(number1, number2)
    elif(operator=='^'):
        result = calc_exponent(number1, number2)
    elif(operator=="s"):
        result = calc_sqrt(number1)
    else:
        print('Uknown operator')
        result = 0
    print('The result is: '+str(result))
    choice = str(input('Would you like to make another calculation? For yes enter y :'))

