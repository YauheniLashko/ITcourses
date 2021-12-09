string_1 = input('Enter your string: ')
num = 'num'
str = 'str'


if string_1.startswith('num'):
    if (string_1[4:].isnumeric() or '.' in string_1):
        string_2 = input('Enter your next string: ')
        print(f'{num}', float(string_1[4:]) + float(string_2[4:]))
    else:
        print('Wrong input')
elif string_1.startswith('string'):
    print(string_1[7:]*3)
else: #string_1 != string_1.startswith('string'):
    if string_1.startswith('True'):
        print('This is TRUE!!!!!')
    elif string_1.startswith('False'):
        print("This is FAAAAAAALSE!")
    else:
        print('Wrong input')



