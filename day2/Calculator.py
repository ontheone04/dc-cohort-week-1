First_num = input('Enter first number:\n')
symbol = input('Enter Operation (+, -, *, /):\n')
Second_num = input('Enter Second Number:\n')

First_num = float(First_num)
Second_num = float(Second_num)

out = None

if symbol == '+':
    out = First_num + Second_num
elif symbol == '-':
    out = First_num - Second_num
elif symbol == '*':
    out = First_num *Second_num
elif symbol == '/':
    out = First_num / Second_num

print('answer: ' + str(out))

