# A check to see if meet the requirements for honour roll
gpa = float(input('What was your Grade Point Average? '))
lowest_grade = float(input('What was your lowest grade? '))

# Boolean variables are TRUE OR FALSE varabils
if gpa >= .85 and lowest_grade >= .70:
	honour_roll = True
else:
	honour_roll = False

# Somewhere later in your code if you need to check if students is 
# on honour roll, all I need to do is check the boolean variable
if honour_roll:
	print('You made honour roll')

############################################################################################

from array import array # Inports arrays
scores = array('d') #makes array
scores.append(97) #Set scores
scores.append(98)
print(scores) #prints scores

############################################################################################

import datetime
# print timestamps after sections of code and sees how long it takers to run its program

first_name = 'Susan'
print('task completed')
print(datetime.datetime.now())
print()

for x in range(0,10):
    print(x)
print('task completed')
print(datetime.datetime.now())
print()