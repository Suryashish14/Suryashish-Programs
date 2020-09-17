print('::::::::::::::::::::::::::: MENU ::::::::::::::::::::::::::::::::::')
print('Press 1 To Check For Armstrong Number')
print('Press 2 To Check For Duck Number')
print('Press 3 To Check For Perfect Number')
print('\t\t\t\t Instructions')
print('''1.Provide Only Positive Numbers
2.For Using The Menu Use Only 1,2,3''')
a=int(input('Enter Your Choice From The Above Menu:'))
if a==1 or a==2 or a==3:
    print(':::::::::::: WELCOME ::::::::::::::::::::')
    if a==1:
        b=int(input('Enter A Number:'))
        numcopy1=b
        add=0
        if b>0:
            while numcopy1>0:
                part=int(numcopy1%10)
                add+=part**3
                numcopy1//=10
            if add==b:
                print('Its an Armstrong Number')
            else:
                print('Its Not An Armstrong Number')
        else:
            print('Invalid Input!Provide Any Positive Integer')
    if a==2:
        c=int(input('Enter Any Positive Number:'))
        numcopy2=c
        flag=0
        if c>0:
            while numcopy2>0:
                rem=int(numcopy2%10)
                numcopy2//=10
                if rem==0:
                    flag+=1
                    break
            if flag>0:
                print(c,'is a Duck Number')
            else:
                print(c,'is Not a Duck Number')
        else:
            print('Invalid Input!Please Provide Any Positive Integer')
    if a==3:
        d=int(input('Enter Any Positive Integer:'))
        numcopy3=d
        factors=0
        if d>0:
            for i in range(1,numcopy3):
                if numcopy3%i==0:
                    factors+=i
            if factors==d:
                print('It is a Perfect Number')
            else:
                print('It is Not A a Perfect Number')    
        else:
            print('invalid Input!Please Enter A Positive Number')
else:
    print('Invalid Input!Please Follow The Instructions')
print('\n')
print('''Thank You For Using This Program..
It Has Developed By Suryashish Guha ''')



            
    


