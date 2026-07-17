#PYTHON CALCULATOR

operator=input('enter an operator(+ - * /):')
num1=float(input('Enter the 1st number:'))
num2=float(input('Enter the 2nd number:'))

if operator=='+':
    result = num1+num2
    print(round(result, 3))
elif operator=='-':
    result = num1-num2
    print(round(result, 3))
elif operator=='*':
    result = num1*num2
    print(round(result, 3))
elif operator=='/':
    result = num1/num2
    print(round(result, 3))
else:
    print(f'{operator} is not a valid operator')

#PYTHON WEIGHT CONVERTER
weight = float(input('enter your weight:'))
unit=input('kilograms or pounds? (K or L):')
if unit=='K':
    weight = weight* 2.205
    unit = 'Lbs.'
    print(f'your weight is {round(weight, 1)}{unit}')
elif unit=='L':
    weight=weight* 2.205
    unit = 'Kgs.'
    print(f'your weight is {round(weight, 1)}{unit}')
else:
    print(f'{unit} is not a valid unit')

#TEMPERATURE CONVERSION
unit=input('Is this temperature in celsius or fahrenheit? (C/F):')
temp=float(input('please enter the temperature:'))

if unit=='C':
    temp = round((9 * temp) / 5 + 32, 1)
    print(f'the temperature in farenheit is: {temp}F')
elif unit=='F':
    temp= round((temp-32)*5/9, 1)
    print(f'the temperature in celsius is:{temp}C')
else:
    print(f'{unit} is not a valid unit')

