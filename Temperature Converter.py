#Temperature Converter(All)
print('::::::::::::::::::MENU:::::::::::::::::::::::::')
print('Press 1 To Convert Celsius To Fahrenheit.')
print('Press 2 To Convert Fahrenheit To Celsius.')
print('Press 3 To Convert Celsius To Kelvin.')
print('Press 4 To Convert Kelvin To Celsius.')
a=int(input('Enter Your Choice -->'))
print("-----------------------Suryashis's Temperature Converter--------------------")
if a==1:
    b=float(input('Enter The Data In Celsius --> '))
    c=b*9/5+32
    print(b,'Degree in Fahrenheit is:',c)
elif a==2:
    d=float(input('Enter The Data In Fahrenheit --> '))
    e=(d-32)*5/9
    print(d,'F in Celsius is:',e)
elif a==3:
    f=float(input('Enter The Data In Celsius --> '))
    g=f+273
    print(f,'Degree in Kelvin is:',g)
elif a==4:
    h=float(input('Enter The Data In Kelvin --> '))
    i=h-273
    print(i,'K in Celsius is:',i)
else:
    print('Invalid Input')
    print('Please Try To Give The Input Within The Range Of The Menu Only!')
#This was Completely Made By Suryashish
