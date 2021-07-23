import random
print('''\t\t\t\t****PASSGEN****
*Press 1 for generating a General Password
*Press 2 for genrating a Password which starts with a uppercase letter 
*Press 3 for generating a password which will surely contain Special Symbols and Digits''')
char='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~!@#$%^&*()_-+={[}]|:;<,>.?/'
char1='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
char2='0123456789~!@#$%^&*()_-+={[}]|:;<,>.?/'
char3='~!@#$%^&*()_-+={[}]|:;<,>.?/'
choice=int(input('Enter Your Choice Here-->'))
password=''
if choice==1:
    for i in range(12):
        password+=char[random.randint(0,89)]#Length of char is 90 so for indexing i have given upper limit as 89.
    print('Here is Your Password:',password)
elif choice==2:
    password+=random.choice(char1)
    for i in range(1,12):
        password+=char[random.randint(0,89)]#Length of char is 90 so for indexing i have given upper limit as 89.
    print('Here is Your Password:',password)
elif choice==3:
    for i in range(2,12):
        password+=char[random.randint(0,89)]#Length of char is 90 so for indexing i have given upper limit as 89.
    password+=random.choice(char2)
    password+=random.choice(char3)
    print('Here is Your Password:',password)
else:
    print('Invalid Input!!Please Try Again')
#Program Terminated Till Further Update