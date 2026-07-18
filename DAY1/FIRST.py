#This is my first python project
#==================
#VARIABLES
#variables = a container for a value(string, integer, float, boolean)
#            A variable behaves asif it is the value it contains.

#strings
#they are a series of texts
first_name = 'srishti'
food = 'sushi'
email = 'srishti123@gmail.com'

#f string (f''/f"") is used to add a text with the variable.
# {} is called a place holder which is used to specify the variable(string/integer/float/boolean) with the added text.

print(f'hello {first_name}')
print(f'your favourite food is : {food}')
print(f'your email is : {email}')

#Integer
# integers are whole numbers(eg: 123 ,2 ,23)
# we can use integers in arithmetic expressions whereas we cannot use strings for the same.
age = 25
quantity = 3
num_of_students = 30

print(f'you are {age} years old')
print(f'you are buying {quantity} kgs of sugar')
print(f'your class has {num_of_students} students')

#Floats
#it is similar to integers but these are the numbers with decimals.
price = 30.44
gpa = 5.5
distance = 3.4

print(f'the price of the sugar is ${price}')
print(f'Your GPA is {gpa}')
print(f'the distance is covered by you is {distance} kms')

#boolean
#it is either true or false.It is mostly used in if/else statements.

is_student = False
for_sale = False #examples
is_online = True #examples

if is_student:
    print('you are a student')
else:
    print('you are not a student')

#====================
#TYPECASTING
#typecasting is the process of converting a variable from one data type to another
#str(), int(), float(), bool()

#eg:
name = 'srishti'
age = 17
gpa = 3.4
is_student = True
#to determine which variable is of what type, we use the type function

print(type(gpa))
#to convert from one data type to another:
age = float(age)

print(age)

#input()=a function that prompts the user to enter data and returns the entire data as a string.
#eg:
name=input('what is your name?:')
age=input('how old are you?:')
gpa=input('how much was your gpa?:')

print(f'Hello {name}!')
print(f'you are {age} years old')
print(f'your gpa is {gpa}')

#===============
#EXERCISE 1ST: RECTANGLE AREA CALC

length = float(input('Enter the length:'))
width = float(input('Enter the width:'))
area = length * width

print(f'the area of the rectangle is {area} cm')

#===============
#EXERCISE 2ND: SHOPPING CART PROGRAM

item= input('what item would u like to buy?:')
price= float(input('what is the price?:'))
quantity= int(input('how many would u like to purchase?:'))
total= price * quantity

print(f'you have bought {quantity} x {item}/s')
print(f'your total amount of price to be paid is ${total}')

