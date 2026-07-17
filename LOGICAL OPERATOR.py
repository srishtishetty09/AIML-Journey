#LOGICAL OPERATORS = EVALUATE MULTIPLE CONDITIONS(or,and,not)
#or=at least one condition has to be true
#and=both conditions must be true
#not=inverts the condition(not True,not False)

#OR
temp=20
is_raining=True
if temp > 35 or temp < 0 or is_raining:
    print('the outdoor event is cancelled')
else:
    print('the outdoor event is still scheduled')
#AND & NOT
temp2=29
is_sunny=True

if temp2>=28 and is_sunny:
    print('It is HOT outside!')
    print('It is SUNNY')
elif temp2<=0 and is_sunny:
    print('It is COLD outside!')
    print('It is SUNNY')
elif 28>temp2>0 and is_sunny:
    print('It is WARM outside!')
    print('It is SUNNY')
elif temp2>=28 and not is_sunny:
    print('It is HOT outside!')
    print('It is CLOUDY')
elif temp2<=0 and not is_sunny:
    print('It is COLD outside!')
    print('It is CLOUDY')
elif 28>temp2>0 and not is_sunny:
    print('It is WARM outside!')
    print('It is CLOUDY')
else:
    print('No update on the weather')


