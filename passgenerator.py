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
save=input('Do you want to save your password(s)[Press y if u want or else press any other key]-->')
passwords=[]
wish='y'
while wish=='y':    
    if choice==1:
        for i in range(12):
            password+=char[random.randint(0,89)]#Length of char is 90 so for indexing i have given upper limit as 89.
        print('Here is Your Password:',password)
        passwords.append(password)
    elif choice==2:
        password+=random.choice(char1)
        for i in range(1,12):
            password+=char[random.randint(0,89)]#Length of char is 90 so for indexing i have given upper limit as 89.
        print('Here is Your Password:',password)
        passwords.append(password)
    elif choice==3:
        for i in range(2,12):
            password+=char[random.randint(0,89)]#Length of char is 90 so for indexing i have given upper limit as 89.
        password+=random.choice(char2)
        password+=random.choice(char3)        
        passwords.append(password)
        print('Here is Your Password:',password)
    else:
        print('Invalid Input!!Please Try Again')
    password=''
    wish=input('If you want to generate another password then press y or else press any other key to terminate the program:')
if save.lower()=='y':    
    f=open('Your Password Log.txt','a+')
    f.write('\t\t\t**Here is your Passwords**\n\n')
    for i in passwords:
        f.write('%s\n'%i)
    f.close()
print('''\n**Thank You For Using PASSGEN**
This Program was made by Suryashish Guha From ACE STUDIOS.
Please Give us Your Feedback at suryashish2005@gmail.com
You Can Also Check out My Site https://suryashish14.github.io/Ace_web_dev/''')
#Program Terminated Till Further Update.