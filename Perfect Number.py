a=int(input('Enter Any Positive Integer:'))
numcopy=a
factors=0
if a>0:
    for i in range(1,numcopy):
        if numcopy%i==0:
            factors+=i
    if factors==a:
        print('It is a Perfect Number')
    else:
        print('It is Not A a Perfect Number')    
else:
    print('invalid Input!Please Enter A Positive Number')
    
