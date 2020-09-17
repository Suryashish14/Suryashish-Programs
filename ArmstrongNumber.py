a=int(input('Enter A Number:'))
numcopy=a
add=0
while numcopy>0:
    part=int(numcopy%10)
    add+=part**3
    numcopy//=10
if add==a:
    print('Its an Armstrong Number')
else:
    print('Its Not An Armstrong Number')