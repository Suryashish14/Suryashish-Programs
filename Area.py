import math
print('::::::::::::::MENU::::::::::::')
print('Press 1 to Get The Area Of A Triangle')
print('Press 2 to Get The Area Of A Rhombus')
print('Press 3 to Get The Area Of A Parallelogram ')
print('Press 4 to Get The Area Of A Trapezoid')
print('\t\t\t\t\t\t\t\tInstructions')
print('1.Please Provide Your Choice In The Range Given By The Above Menu')
print('2.Please Provide All The Values ')
choice=int(input('Enter Your Choice:'))
if choice==1:
    a=float(input('Enter The Length Of the First Side:'))
    b=float(input('Enter The Length Of the Second Side:'))
    c=float(input('Enter The Length Of the Third Side:'))
    if a>0 and b>0 and c>0:
        semiperimeter=(a+b+c)/2
        s=semiperimeter
        area=math.sqrt((s)*(s-a)*(s-b)*(s-c))
        print(area)
    else:
        print('Invalid Input!')
   
elif choice==2:
    a=float(input('Enter The Length Of One Side:'))
    b=float(input('Enter The Length Of The Altitude:'))
    if a>0 and b>0:
        area=a*b
        print(area)
    else:
        print('Invalid Input!')
elif choice==3:
    a=float(input('Enter The Length Of The Height:'))
    b=float(input('Enter The Length Of The Base:'))
    if a>0 and b>0:
        area=a*b
        print(area)
    else:
        print('Invalid Input!')
elif choice==4:
    a=float(input('Enter The Length Of The Lower Base:'))
    b=float(input('Enter The Lenth Of The Upper Base:'))
    c=float(input('Enter The Height Of The Trapezoid:'))
    if a>0 and b>0 and c>0:
        area=((a+b)/2)*c
        print(area)
    else:
        print('Invalid Input!')
else:
    print('Invalid Input!Please Press The Keys According To Given Menu')
    


