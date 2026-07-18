
#friends= 5

#AUGMENTED ASSIGNMENT OPERATORS
#augmented assignment operators require less coding and is easier to read
#ADDITION
#friends= friends+1  (normal)
#friends += 1  (augmented assignment operator)
#SUBTRACTION
#friends= friends-1  (normal)
#friends -= 1  (augmented assignment operator)
#MULTIPLICATION
#friends= friends*3  (normal)
#friends *= 3  (augmented assignment operator)
#DIVISION
#friends= friends/2  (normal)
#friends /= 2  (augmented assignment operator)
#EXPONENTS
#friends= friends ** 2  (normal)
#friends **= 2 (augmented assignment operator)
#MODULUS
#remainder= friends % 2

#print(friends)
#====================
#MATH FUNCTIONS
x= 3.14
y= -4
z= 5
result=round(x) #ROUND FUNCTION
result2=abs(y) #ABSOLUTE VALUE FUNCTION(IT IS THE DISTANCE AWAY FRON ZERO AS A WHOLE NUMBER)
result3=pow(5,2)#POWER FUNCTION(X[THE NUMBER/BASE],Y[THE POWER])
result4= max(2,4,10)#MAXIMUM VALUE OUT OF THE LOT
result5=min(10,40,2,3)#MINIMUM VALUE OUT OF THE LOT

print(result)
print(result2)
print(result3)
print(result4)
print(result5)

import math
z=87.4
print(math.pi)
print(math.e)
print(math.log)
print(math.sin)
resultA=math.ceil(z) #rounds the number up
resultB=math.floor(z) #rounds the number down
print(resultB)

#MAKE A PROGRAM TO FIND THE CIRCUMFERENCE OF THE CIRCLE
#FORMULA IS = (C=2piR)
radius = float(input('enter a radius:'))
circumference= 2 * math.pi * radius
print(f'the circumference of the circle is {circumference} cms')

#MAKE A PROGRAM TO FIND THE AREA OF THE CIRCLE
#FORMULA IS = (A=piR^2)
radius2 = float(input('enter a radius:'))
area= math.pi * pow(radius2,2)
print(f'the area of this circle is {round(area,2)} cms')

#MAKE A PROGRAM TO FIND THE HYPOTENUSE OF A RIGHT ANGLE
import math
A=float(input('enter side A:'))
B=float(input('enter side B:'))
c=math.sqrt(pow(A,2) + pow(B,2))
print(f'side C of the right angle is {round(c,2)} cms')

