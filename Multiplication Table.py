#Suryashish's Multiplication Table
a=int(input('Enter A Number:'))
lower=int(input('Enter The Lower Limit Of The Range:'))
up=int(input('Enter The Upper Limit Of The Range:'))
print('\t\t\t\t\t\t\t Multiplication Table For',a)
numcopy=a
if numcopy>0:
    for number in  range(lower,up+1):
        print(numcopy,'X',number,'=',numcopy*number)
else:
    print('Invalid Input!Please Give Any Positive Integer ')