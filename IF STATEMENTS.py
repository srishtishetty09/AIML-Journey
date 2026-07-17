#if= do some code only 'IF' some condition is true
#    'ELSE' do something else

#SIGN UP DEPENDING ON AGE
age =int(input('enter your age:'))
if age>=100:
    print('you are too old to sign up!')
elif age>=18:
    print('you are now signed up!')
elif age<0:
    print('you havent been born yet')
else:
    print('you are not signed up as you must be 18/18+ to sign up')

#FOOD RESPONSE
response= input('would you like food?(yes/no):')
if response=='yes':
    print('Have some food!')
else:
    print('Sorry, no food for you')
#NAME
name=input('enter your name:')
if name=='':
    print('u did not enter a name')
else:
    print('Hi, wasup!')
#BOOLEAN
online=True
if online:
    print('you are online')
else:
    print('you are offline')

