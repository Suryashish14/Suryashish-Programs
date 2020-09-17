a=int(input('Enter Any Positive Integer:'))
numcopy=a
for i in range(1,numcopy):
    if numcopy%i==0:
        print(i,end=',')
print(a)



