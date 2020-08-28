#First Attemmpt To Create  A Calculator
print(':::::::::::::::: MENU :::::::::::::::::::::')
print('Press 1 For Addition')
print('Press 2 For Sustraction')
print('Press 3 For Multiplication')
print('Press 4 For Division')
a=int(input('Enter Your Choice Here:'))
print("\t\t\t\t\t\t\tSuryashish's Calculator")
if a==1:
    num1=int(input('Enter A Number -->' ))
    num2=int(input('Enter A Number -->'))
    num3=num1+num2
    print(num1,'+',num2,'=',num3)
elif a==2:
    num4=int(input('Enter A Number -->'))
    num5=int(input('Enter A Number -->'))
    num6=num4-num5
    print(num4,'-',num5,'=',num6)
elif a==3:
    num7=int(input('Enter A Number -->'))
    num8=int(input('Enter A Number -->'))
    num9=num8*num7
    print(num7,'*',num8,'=',num9)
elif a==4:
    num10=int(input('Enter A Number -->' ))
    num11=int(input('Enter A Number -->'))
    if num11==0:
        print('Error! number cannot be divided by 0 ')
    else:    
        num12=num10/num11
        print(num10,'Divided By',num11,'=',num12)
else:
    print("Invalid Input.Please Press An Valid Input.")
#Program Concluded After 1 Hour!!!
