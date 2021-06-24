def addition(num1,num2):
    num3=num1+num2
    print(num1,'+',num2,'=',num3)
def substraction(num1,num2):
    if num1>=num2:
        num3=num1-num2
        print(num1,'-',num2,'=',num3)
    elif num1<num2:
        num3=num2-num1
        print(num2,'-',num1,'=',num3)
def multiplication(num1,num2):
    num3=num1*num2
    print(num1,'*',num2,'=',num3)
def division(num1,num2):
    if num1==0:
        print(' 0 ')
    elif num2==0:
        print('A Number Cannot Be Divided By 0')
    else:    
        num3=num1/num2
        print(num1,'Divided By',num2,'=',num3)
