def SpecialNumber(): 
    a=int(input('Enter A Number:'))
    numcopy=a
    b=a
    c=a
    sum=0
    while numcopy > 0:
        remainder=numcopy%10
        sum+=remainder
        numcopy=numcopy//10

    product=1
    while b > 0:
        remainder=b%10
        product=product*remainder
        b=b//10
#Calculating The Total Sum
    total_sum=sum+product
#Putting The Condition
if SpecialNumber()==c:
    print('It is a Special Number')
else :
    print('It is not a Special Number')