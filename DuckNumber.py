a=int(input('Enter Any Positive Number:'))
numcopy=a
flag=0
if a>0:
    while numcopy>0:
        rem=int(numcopy%10)
        numcopy//=10
        if rem==0:
            flag+=1
            break
    if flag>0:
        print(a,'is a Duck Number')
    else:
        print(a,'is Not a Duck Number')
else:
    print('Invalid Input!Please Provide Any Positive Integer')