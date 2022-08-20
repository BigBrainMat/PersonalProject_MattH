# A check to see if meet the requirements for honour roll
gpa = float(input('What was your Grade Point Average? '))
lowest_grade = float(input('What was your lowest grade? '))

# Boolean variables are TRUE OR FALSE varabils
if gpa >= .85 and lowest_grade >= .70:
	honour_roll = True
else:
	honour_roll = False

# this will check to see true or false to determine honour roll
if honour_roll:
	print('You made honour roll')
