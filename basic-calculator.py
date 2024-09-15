num1 = int(input('Enter your first number: '))
num2 =int( input('Enter your second number: '))
operators = '+ , - , * , /'
choices = input('Enter your operator(+, - , * , /): ')
if choices == '+':
    print(num1 + num2)
elif choices == '-':
    print(num1 - num2) 
elif choices == '*':
    print(num1 * num2)
elif choices == '/':
    print(num1 / num2)
else :
    print('Invalid operator.')