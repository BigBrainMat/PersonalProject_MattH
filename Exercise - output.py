print('Hello World!') 
# (output) Hello World!

PI = 3.14
print(PI)
# (output) 3.14

# Reading keyboard input #

name = input('Enter your name:')
print(name)
# (output) What ever you typed in as your name EX: Matthew

print('What is your name?')
name = input()
print(name)
# (output) What ever you typed in as your name EX: Matthew

# Reading numbers as input #

x = input('Enter a number: ')
print(type(x))
# (output) <class 'int'>

x = int(input('Enter a number: '))
print(type(x))
# (output) <class 'int'>

# Converting numbers to strings #

x = 5
print('The number is ' + str(x))
# (output) The number is 5